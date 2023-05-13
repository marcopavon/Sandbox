const sqlite3 = require("sqlite3").verbose()
const md5 = require("md5")
const DBSOURCE = "./express-sqlite/database.db"

db = new sqlite3.Database(DBSOURCE)

module.exports = db
