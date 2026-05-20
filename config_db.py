from chainlit.data.sql_alchemy import SQLAlchemyDataLayer
import chainlit as cl
import asyncio
import aiosqlite

async def create_tables():
    async with aiosqlite.connect("quria_history.db") as db:
        await db.execute("""CREATE TABLE IF NOT EXISTS users (
            id TEXT PRIMARY KEY, identifier TEXT, "createdAt" TEXT, metadata TEXT)""")
        await db.execute("""CREATE TABLE IF NOT EXISTS threads (
            id TEXT PRIMARY KEY, "createdAt" TEXT, name TEXT, "userId" TEXT, 
            "userIdentifier" TEXT, tags TEXT, metadata TEXT)""")
        await db.execute("""CREATE TABLE IF NOT EXISTS steps (
            id TEXT PRIMARY KEY, name TEXT, type TEXT, "threadId" TEXT,
            "parentId" TEXT, "disableFeedback" INTEGER, streaming INTEGER,
            waitForAnswer INTEGER, "isError" INTEGER, metadata TEXT,
            tags TEXT, input TEXT, output TEXT, "createdAt" TEXT,
            start TEXT, end TEXT)""")
        await db.execute("""CREATE TABLE IF NOT EXISTS elements (
            id TEXT PRIMARY KEY, "threadId" TEXT, type TEXT, url TEXT,
            "chainlitKey" TEXT, name TEXT, display TEXT, language TEXT,
            page INTEGER, size TEXT, "forId" TEXT, mime TEXT)""")
        await db.commit()

asyncio.run(create_tables())

@cl.data_layer
def get_data_layer():
    return SQLAlchemyDataLayer(conninfo="sqlite+aiosqlite:///quria_history.db")