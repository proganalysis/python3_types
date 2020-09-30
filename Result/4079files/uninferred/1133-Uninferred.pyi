from typing import Any

revision: str
down_revision: Any
branch_labels: Any
depends_on: Any

def upgrade() -> None: ...
def downgrade() -> None: ...
