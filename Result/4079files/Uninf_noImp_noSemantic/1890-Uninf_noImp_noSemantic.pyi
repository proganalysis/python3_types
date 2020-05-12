from alembic import op as op
from typing import Any

revision: str
down_revision: Any

def upgrade() -> None: ...
def downgrade() -> None: ...
