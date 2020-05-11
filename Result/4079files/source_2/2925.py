import os
import argparse
from multiprocessing.pool import Pool
from typing import Tuple, Dict, Any

import tensorflow as tf

tf.enable_eager_execution()

parser = argparse.ArgumentParser()
parser.add_argument('--img_height', type=int, default=1080)
parser.add_argument('--img_width', type=int, default=1980)
parser.add_argument('--num_workers', type=int, default=18)
parser.add_argument('--input_path', type=str, default='gs://catdraw/ai_SOURCE')
parser.add_argument('--output_path', type=str, default='data/catdraw')
args = parser.parse_args()


def parse_img(rough: tf.Tensor, clean: tf.Tensor, color: tf.Tensor) -> Tuple[tf.Tensor, ...]:
    rough_img = tf.image.decode_png(tf.read_file(rough), channels=3)
    clean_img = tf.image.decode_png(tf.read_file(clean), channels=3)
    detail_img = tf.image.decode_png(tf.read_file(color), channels=3)

    rough_grayscale = tf.image.resize_images(
        images=tf.image.rgb_to_grayscale(rough_img),
        size=[args.img_height, args.img_width])
    clean_grayscale = tf.image.resize_images(
        images=tf.image.rgb_to_grayscale(clean_img),
        size=[args.img_height, args.img_width])

    rough_scaled_grayscale = tf.where(condition=tf.equal(rough_grayscale, tf.zeros((1, 1, 1), dtype=tf.float32)),
                                      x=tf.zeros(shape=(args.img_height, args.img_width, 1)),
                                      y=tf.constant(255.0, shape=(args.img_height, args.img_width, 1)))
    clean_scaled_grayscale = tf.where(condition=tf.equal(clean_grayscale, tf.zeros((1, 1, 1), dtype=tf.float32)),
                                      x=tf.zeros(shape=(args.img_height, args.img_width, 1)),
                                      y=tf.constant(255.0, shape=(args.img_height, args.img_width, 1)))

    return rough_scaled_grayscale, clean_scaled_grayscale, clean_img, detail_img


def dedup(input_dir: str) -> Dict[str, Any]:
    rough_files = tf.gfile.ListDirectory(os.path.join(args.input_path, input_dir, 'rough'))
    clean_files = tf.gfile.ListDirectory(os.path.join(args.input_path, input_dir, 'cleanLine'))
    color_files = tf.gfile.ListDirectory(os.path.join(args.input_path, input_dir, 'color'))

    # get dedup indices from the rough dir
    fnames_dedup = [[], [], []]
    b_last = None
    for i, fname in enumerate(rough_files):
        full_fname = os.path.join(args.input_path, input_dir, 'rough', fname)
        b = tf.gfile.Stat(full_fname).length
        if b != b_last:
            fnames_dedup[0].append(full_fname)
            full_fname_clean = os.path.join(args.input_path, input_dir, 'cleanLine', clean_files[i])
            fnames_dedup[1].append(full_fname_clean)
            full_fname_color = os.path.join(args.input_path, input_dir, 'color', color_files[i])
            fnames_dedup[2].append(full_fname_color)
        b_last = b

    print(f'Dedup\'d from {i} records to {len(fnames_dedup[0])} records in {input_dir}')

    assert len(fnames_dedup[0]) == len(fnames_dedup[1])
    assert len(fnames_dedup[1]) == len(fnames_dedup[2])

    return {
        'scene': input_dir.strip('/'),
        'fnames': zip(*fnames_dedup)
    }


def write_tf_records(data: Dict[str, Any]) -> None:
    os.makedirs(args.output_path, exist_ok=True)
    output_s_file = os.path.join(args.output_path, f"{data['scene']}.record")
    writer = tf.python_io.TFRecordWriter(output_s_file)

    for i, fnames in enumerate(data['fnames']):
        rough_gray, clean_gray, clean_color, detail_color = parse_img(*fnames)
        tf_example = tf.train.Example(features=tf.train.Features(feature={
            'scene': tf.train.Feature(
                bytes_list=tf.train.BytesList(value=[tf.compat.as_bytes(data['scene'])])),
            'scene_number': tf.train.Feature(
                bytes_list=tf.train.Int64List(value=[data['scene_number']])),
            'image/rough_gray': tf.train.Feature(
                bytes_list=tf.train.BytesList(value=[rough_gray.numpy().tostring()])),
            'image/clean_gray': tf.train.Feature(
                bytes_list=tf.train.BytesList(value=[clean_gray.numpy().tostring()])),
            'image/clean_color': tf.train.Feature(
                bytes_list=tf.train.BytesList(value=[clean_color.numpy().tostring()])),
            'image/detail_color': tf.train.Feature(
                bytes_list=tf.train.BytesList(value=[detail_color.numpy().tostring()]))
        }))
        writer.write(tf_example.SerializeToString())

    print(f'Wrote {i} images to {output_s_file}')
    writer.close()


if __name__ == '__main__':
    with tf.device('/cpu:0'):
        p = Pool(args.num_workers)

        scenes = tf.gfile.ListDirectory(args.input_path)
        del scenes[3]  # scene 100 does not have clean images

        input_chunks = p.map(dedup, scenes)

        # add a unique scene number to each input_chunk starting from 0
        for i, chunk in enumerate(input_chunks):
            chunk['scene_number'] = i

        train_ds = p.map(write_tf_records, input_chunks)

        p.close()
