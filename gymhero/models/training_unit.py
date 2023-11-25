from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Table, func
from sqlalchemy.orm import relationship

from gymhero.database.base_class import Base

training_unit_exercise = Table(
    "training_unit_exercise",
    Base.metadata,
    Column("training_unit_id", ForeignKey("training_units.id"), primary_key=True),
    Column("exercise_id", ForeignKey("exercises.id"), primary_key=True),
)


class TrainingUnit(Base):
    __tablename__ = "training_units"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )
    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User")
    exercises = relationship("Exercise", secondary=training_unit_exercise)

    def __repr__(self):
        return f"TrainingUnit(id={self.id}, name={self.name})"
