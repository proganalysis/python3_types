# built-in modules
import os
from itertools import chain

# installed modules
import numpy
from keras.callbacks import Callback
import keras.backend as K
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# project modules
from .meta import time_formatter, timer


class NotSoChattyLogger(Callback):
    def __init__(self, print_every=1000000,
                 start=None, counter=None, metrics=None):
        self._print_every = print_every
        self._partial_counter = 0
        self._total_counter = counter if counter is not None else 0
        self._start = start if start is not None else timer()
        self._metrics = {m: [] for m in (metrics if metrics else {})}
        self._epoch = 0
        super(NotSoChattyLogger, self).__init__()

    @property
    def start(self):
        return self._start

    @property
    def epoch(self):
        return self._epoch

    @epoch.setter
    def epoch(self, epoch):
        self._epoch = epoch

    def __getitem__(self, item):
        return self._metrics[item]

    @property
    def count(self):
        return self._total_counter

    def on_batch_end(self, batch, logs={}):
        self._partial_counter += logs.get('size', 0)
        self._total_counter += logs.get('size', 0)

        if self._partial_counter >= self._print_every:
            [
                self._metrics[k].append(v)
                for k, v in logs.items() if k in self._metrics
            ]

            current_logs = {
                k: v[-1] for k, v in sorted(self._metrics.items()) if v
            }

            delta = timer() - self._start
            metrics = ' - '.join(
                '{}: {:.1e}'.format(m, float(v))
                for m, v in current_logs.items()
            )

            print(
                '[keras] epoch {}: {:,} trained in {} ({:.1e} s/example) – {}'
                ''.format(
                    self.epoch, self._total_counter, time_formatter(delta),
                    delta / self._total_counter, metrics
                )
            )
            self._partial_counter = 0


def plot_weights(model, dest_dir, layers=None):
    for layer in model.layers:
        if layers is not None and layer not in layers:
            continue

        try:
            W, b = model.get_layer(layer.name).get_weights()
        except ValueError:
            # this is not a model with weights (e.g. noise layer)
            continue

        dead_connections = sum(
            1 if w < K.epsilon() else 0 for w in numpy.nditer(W)
        )
        dead_connections_percent = dead_connections / numpy.prod(W.shape)

        print('[analysis] layer {}: {:,} dead connections ({:.1%})'.format(
            layer.name, dead_connections, dead_connections_percent
        ))

        cmap_range = max(
            numpy.max(W), numpy.abs(numpy.min(W)),
            numpy.max(b), numpy.abs(numpy.min(b)),
        )

        b = b.reshape(b.shape[0], 1) @ numpy.ones((1, 10))

        fig, (ax1, ax2) = plt.subplots(1, 2, sharey=False)

        fig.suptitle(
            'Weights {}'.format(layer.name), fontsize=16, fontweight='bold'
        )

        cax1 = ax1.imshow(
            W, cmap='coolwarm', interpolation='nearest',
            vmin=-cmap_range, vmax=cmap_range, origin='lower'
        )
        x, y = W.shape
        ax1.set_ylim([0, x])
        ax1.set_xlim([0, y])
        ax1.set_title('Weights')
        ax1.set_ylabel('input')
        ax1.set_xlabel('output')

        for t in chain(ax1.xaxis.get_ticklines(), ax1.yaxis.get_ticklines()):
            t.set_visible(False)

        ax2.imshow(
            b, cmap='coolwarm', interpolation='nearest',
            vmin=-cmap_range, vmax=cmap_range, origin='lower'
        )
        ax2.set_title('Bias')
        ax2.set_xticks([])
        for t in chain(ax2.xaxis.get_ticklines(), ax2.yaxis.get_ticklines()):
            t.set_visible(False)
        ax2.set_ylabel('output')

        cbar = fig.colorbar(cax1, ticks=[-cmap_range, 0, cmap_range])
        cbar.ax.set_yticklabels(
            ['{:.1e}'.format(-cmap_range), ' 0', '{:.1e}'.format(cmap_range)]
        )

        output_fn = os.path.join(
            dest_dir, '{}-{}.pdf'.format(model.name, layer.name)
        )
        fig.savefig(output_fn)
        fig.clf()

