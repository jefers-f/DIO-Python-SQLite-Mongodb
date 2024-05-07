from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, inspect, select

Base = declarative_base()


class User(Base):
    __tablename__ = 'user_account'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    address = relationship(
        'Address', back_populates='user', cascade='all, delete-orphan'
    )

    def __repr__(self):
        return f'User (id={self.id}, name={self.name}, fullname={self.fullname})'


class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True, autoincrement=True)
    email_address = Column(String(30), nullable=False)
    user_id = Column(Integer, ForeignKey('user_account.id'), nullable=False)

    user = relationship(
        'User', back_populates='address'
    )

    def __repr__(self):
        return f'Address (id={self.id}, email={self.email_address})'


engine = create_engine('sqlite://')
Base.metadata.create_all(engine)

inspector_engine = inspect(engine)
print(inspector_engine.get_table_names())

Session = sessionmaker(bind=engine)

with Session() as session:
    jeferson = User(
        name='jeferson',
        fullname='jeferson farias',
        address=[Address(email_address='jfarcdt@gmail')]
    )

    joao = User(
        name='joao',
        fullname='joao farias',
        address=[Address(email_address='joao@gmail')]
    )

    juca = User(
        name='juca',
        fullname='juca bala'
    )

    session.add_all([jeferson, joao, juca])
    session.commit()

stmt = select(User).where(User.name.in_(['jeferson', 'joao']))
for user in session.scalars(stmt):
    print(user)

stmt_adress = select(Address)
for address in session.scalars((stmt_adress)):
    print(address)