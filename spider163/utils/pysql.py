#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer, String, DateTime, Index
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.sql import func
from sqlalchemy.dialects.mysql import MEDIUMTEXT
import config

Base = declarative_base()


class Playlist163(Base):
    __tablename__ = "playlist163"

    id = Column(Integer(), primary_key=True, autoincrement=True)
    title = Column(String(255), server_default="System Title")
    link = Column(String(255), server_default="No Link")
    cnt = Column(Integer(), server_default="-1")
    dsc = Column(String(255), server_default="No Description")
    create_time = Column(DateTime, server_default=func.now())
    over = Column(String(255), server_default="N")
    over_link = Index("over_link", over, link)


class Music163(Base):
    __tablename__ = "music163"
    id = Column(Integer(),primary_key=True, autoincrement=True)
    song_id = Column(Integer())
    song_name = Column(String(300), server_default="No Name")
    author = Column(String(300), server_default="No Author")
    over = Column(String(255), server_default="N")
    create_time = Column(DateTime, server_default=func.now())
    comment = Column(Integer(), server_default="-1")
    over_id = Index("over_id", over,id)
    key_author = Index("author", author)
    song_id_comment = Index("song_id_comment", song_id, comment)


class Comment163(Base):
    __tablename__ = "comment163"
    id = Column(Integer(), primary_key=True, autoincrement=True)
    song_id = Column(Integer())
    txt = Column(MEDIUMTEXT)
    author = Column(String(300), server_default="No Author")
    liked = Column(Integer(), server_default="0")
    Index("liked_song_id", liked, song_id)
    Index("song_id_liked", song_id, liked)


class Lyric163(Base):
    __tablename__ = "lyric163"
    id = Column(Integer(), primary_key=True, autoincrement=True)
    song_id = Column(Integer())
    txt = Column(MEDIUMTEXT)
    key_song_id = Index("song_id", song_id)


engine = create_engine(config.get_db(), convert_unicode=True, echo=True)


def single(table, k, v):
    cnt = engine.execute('select count(*) from ' + table + ' where ' + k + '="' + v + '"').fetchone()
    if cnt[0] == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    Base.metadata.create_all(engine)
    print(single("playlist163", "link", "sd"))
