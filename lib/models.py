from sqlalchemy import ForeignKey, Column, Integer, String, Boolean, MetaData
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

class Role(Base):
    __tablename__ = "roles"
    
    id = Column(Integer, primary_key=True)
    character_name = Column(String())
    
    @property
    def actors(self):
        return [a.actor for a in self.auditions]

    # Returns a list of locations from auditions for this role
    @property
    def locations(self):
        return [a.location for a in self.auditions]

    # Returns the first hired audition or a message
    def lead(self):
        hired_auditions = [a for a in self.auditions if a.hired]
        if hired_auditions:
            return hired_auditions[0]
        return "no actor has been hired for this role"

    # Returns the second hired audition (understudy) or a message
    def understudy(self):
        hired_auditions = [a for a in self.auditions if a.hired]
        if len(hired_auditions) >= 2:
            return hired_auditions[1]
        return "no actor has been hired for understudy for this role"

class Audition(Base):
    __tablename__ = 'auditions'
    
    id = Column(Integer(), primary_key=True)
    actor = Column(String())
    location = Column(String())
    phone = Column(Integer())
    hired = Column(Boolean(), default=False)
    
    role_id =  Column(Integer(), ForeignKey("roles.id"))
    
     def call_back(self):
        self.hired = True
    