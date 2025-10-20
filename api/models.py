from sqlalchemy import Column, Integer, String, BigInteger, DateTime, func, ForeignKey, text, Boolean
from sqlalchemy.orm import declarative_base 
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.sql import func 

Base = declarative_base()

'''
Edits that might need to be made
- attributes in the items table, might just be notes
- userInvs table did not have .inv during queries

'''
class Users(Base):
  __tablename__ = "users"
  __table_args__ = {'schema': 'inv'}
  
  userid = Column(BigInteger, primary_key=True )
  username = Column(String, unique=True, nullable=False)
  password = Column(String, nullable=False)
  email = Column(String, unique=True, nullable=False) 
  created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
  updated_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False, onupdate=func.now())
  deleted_at = Column(DateTime(timezone=True), nullable=True)
  firstname = Column(String, nullable=False)
  lastname = Column(String, nullable=False)
  
class Skeletons(Base):
  __tablename__ = "skeletons"
  __table_args__ = {'schema': 'inv'}
  
  skeleid = Column(BigInteger, primary_key=True)
  skelename = Column(String, nullable=False)
  imgpath = Column(String)
  attributes = Column(JSONB, nullable=True, server_default=text("'{}'::jsonb") )
  creatorid = Column(BigInteger,
                     ForeignKey("inv.users.userid",
                     ondelete="SET NULL", onupdate="CASCADE"),
                     nullable=True)
  posted = Column(Boolean, server_default=text('false'))
  created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
  updated_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False, onupdate=func.now())
  deleted_at = Column(DateTime(timezone=True), nullable=True)

class Inventories(Base):
  __tablename__ = "inventories"
  __table_args__ = {'schema': 'inv'}
  
  invid = Column(BigInteger, primary_key=True)
  invname = Column(String, nullable=False)
  ownerid = Column(BigInteger, 
                   ForeignKey("inv.users.userid", 
                   ondelete="restrict", onupdate="cascade"),
                   nullable=False)
  parentinvid = Column(BigInteger, 
                       ForeignKey("inv.inventories.invid",
                       ondelete="cascade", onupdate="cascade"),
                       nullable=True)
  imgpath = Column(String, nullable=True)
  created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
  updated_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False, onupdate=func.now())
  deleted_at = Column(DateTime(timezone=True), nullable=True)
  
class Folders(Base):
  __tablename__ = "folders"
  __table_args__ = {'schema': 'inv'}
  
  folderid = Column(BigInteger, primary_key=True)
  foldername = Column(String, nullable=False)
  invid = Column(BigInteger, 
                 ForeignKey("inv.inventories.invid",
                 onupdate="cascade", ondelete="cascade"),
                 nullable=False)
  parentfolderid = Column(BigInteger, 
                          ForeignKey("inv.folders.folderid",
                          onupdate="cascade", ondelete="cascade"),
                          nullable=True)
  imgpath = Column(String, nullable=True)
  created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
  updated_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False, onupdate=func.now())
  deleted_at = Column(DateTime(timezone=True), nullable=True)
  
class Statuses(Base):
  __tablename__ = "statuses"
  __table_args__= {'schema': 'inv'}
  
  statusid = Column(BigInteger, primary_key=True)
  statusname = Column(String, nullable=False)
  imgpath = Column(String, nullable=False)
  doesitcount = Column(Boolean, nullable=False, server_default=text('false'))
  creatorid = Column(BigInteger,
                     ForeignKey("inv.users.userid",
                     ondelete="set null", onupdate="cascade"),
                     nullable=True)
  
class SkeleInstances(Base):
  __tablename__ = "skeleinstances"
  __table_args__ = {'schema': 'inv'}
  
  skeleinstanceid = Column(BigInteger, primary_key=True)
  skeleid = Column(BigInteger,
                   ForeignKey("inv.skeletons.skeleid",
                   onupdate="restrict", ondelete="restrict"),
                   nullable=False)
  invid = Column(BigInteger,
                 ForeignKey("inv.inventories.invid",
                 onupdate="cascade", ondelete="cascade"),
                 nullable=False)
  folderid = Column(BigInteger,
                    ForeignKey("inv.folders.folderid",
                    onupdate="set null", ondelete="set null"),
                    nullable=True)
  count = Column(Integer, nullable = False)
  
class Items(Base):
  __tablename__ = "items"
  __table_args__ = {'schema': 'inv'}
  
  itemid = Column(BigInteger, primary_key=True)
  skeleinstanceid = Column(BigInteger, 
                          ForeignKey("inv.skeleinstances.skeleinstanceid",
                          onupdate="cascade", ondelete="cascade"),
                          nullable=False)
  parentitemid = Column(BigInteger, 
                        ForeignKey("inv.items.itemid",
                        ondelete="set null", onupdate="cascade"),
                        nullable=True)
  statusid = Column(BigInteger,
                    ForeignKey("inv.statuses.statusid", 
                    ondelete="set default", onupdate="cascade"),
                    nullable=False,
                    server_default=text('0'))
  creatorid = Column(BigInteger,
                     ForeignKey("inv.users.userid",
                     ondelete="set null", onupdate="cascade"),
                     nullable=True)
  attributes = Column(JSONB, nullable=False, server_default=text("'{}'::jsonb"))
  notes = Column(String, nullable=True)
  created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
  updated_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False, onupdate=func.now())
  deleted_at = Column(DateTime(timezone=True), nullable=True)
                    
class UserRoles(Base):
  __tablename__ = "userroles"
  __table_args__ = {'schema': 'inv'}
  
  roleid = Column(Integer, primary_key=True)
  rolename = Column(String, nullable=False, unique=True)
  canupdownsuper = Column(Boolean, nullable=False, server_default=text("false"))
  canupdownadmin = Column(Boolean, nullable=False, server_default=text("false"))
  caninvite = Column(Boolean, nullable=False, server_default=text("false"))
  canwrite = Column(Boolean, nullable=False, server_default=text("false"))
  
class UserInvs(Base):
  __tablename__ = "userinvs"
  __table_args__ = {'schema': 'inv'}
  
  userid = Column(BigInteger, 
                  ForeignKey("inv.users.userid", 
                  ondelete="cascade", onupdate="cascade"),
                  primary_key=True)
  invid = Column(BigInteger,
                 ForeignKey("inv.inventories.invid", 
                 ondelete="cascade", onupdate="cascade"),
                 primary_key=True)
  roleid = Column(Integer, 
                  ForeignKey("inv.userroles.roleid",
                  ondelete="set default", onupdate="cascade"),
                  nullable=False, server_default=text('4'))

class UserSkelesFav(Base):
  __tablename__ = "userskelesfav"
  __table_args__ = {'schema': 'inv'}
  
  userid = Column(BigInteger, 
                  ForeignKey("inv.users.userid", 
                  ondelete="cascade", onupdate="cascade"),
                  primary_key=True)
  skeleid = Column(BigInteger,
                    ForeignKey("inv.skeletons.skeleid",
                    ondelete="cascade", onupdate="cascade"),
                    primary_key=True)
  
class UserStatusFav(Base):
  __tablename__ = "userstatusfav"
  __table_args__ = {'schema': 'inv'}
  
  userid = Column(BigInteger, 
                  ForeignKey("inv.users.userid", 
                  ondelete="cascade", onupdate="cascade"),
                  primary_key=True)
  statusid = Column(BigInteger,
                    ForeignKey("inv.statuses.statusid",
                    ondelete="cascade", onupdate="cascade"),
                    primary_key=True)
  
  class SkeleParents(Base):
    __tablename__ = "skeleparents"
    __table_args__ = {'schema': 'inv'}
    
    skeleid = Column(BigInteger,
                    ForeignKey("inv.skeletons.skeleid",
                    ondelete="cascade", onupdate="cascade"),
                    primary_key=True)
    parentskeleid = Column(BigInteger,
                    ForeignKey("inv.skeletons.skeleid",
                    ondelete="cascade", onupdate="cascade"),
                    primary_key=True)
class SkeleChildren(Base):
  __tablename__ = "skelechildren"
  __table_args__ = {'schema': 'inv'}
  
  skeleid = Column(BigInteger,
                    ForeignKey("inv.skeletons.skeleid",
                    ondelete="cascade", onupdate="cascade"),
                    primary_key=True)
  childskeleid = Column(BigInteger,
                  ForeignKey("inv.skeletons.skeleid",
                  ondelete="cascade", onupdate="cascade"),
                  primary_key=True)
  
class SkeleFolders(Base):
  __tablename__ = "skelefolders"
  __table_args__ = {'schema': 'inv'}
  
  skeleid = Column(BigInteger,
                    ForeignKey("inv.skeletons.skeleid",
                    ondelete="cascade", onupdate="cascade"),
                    primary_key=True)
  folderid = Column(BigInteger,
                    ForeignKey("inv.folders.folderid",
                    ondelete="cascade", onupdate="cascade"),
                    primary_key=True)
  
class InvSkeles(Base):
  __tablename__ = "invskeles"
  __table_args__ = {'schema': 'inv'}
  
  invid = Column(BigInteger,
                 ForeignKey("inv.inventories.invid",
                 ondelete="cascade", onupdate="cascade"),
                 primary_key=True)
  skeleid = Column(BigInteger,
                  ForeignKey("inv.skeletons.skeleid",
                  ondelete="cascade", onupdate="cascade"),
                  primary_key=True)
  
class InvStatuses(Base):
  __tablename__ = "invstatuses"
  __table_args__ = {'schema': 'inv'}
  
  invid = Column(BigInteger,
                 ForeignKey("inv.inventories.invid",
                 ondelete="cascade", onupdate="cascade"),
                 primary_key=True)
  statusid = Column(BigInteger,
                    ForeignKey("inv.statuses.statusid",
                    ondelete="cascade", onupdate="cascade"),
                    primary_key=True)
  
class FolderSkeles(Base):
  __tablename__ = "folderskeles"
  __table_args__ = {'schema': 'inv'}
  
  folderid = Column(BigInteger,
                    ForeignKey("inv.folders.folderid",
                    ondelete="cascade", onupdate="cascade"),
                    primary_key=True)
  skeleinstanceid = Column(BigInteger, 
                           ForeignKey("inv.skeleisntances.skeleinstanceid",
                           ondelete="cascade", onupdate="cascade"),
                           primary_key=True)