const sqlite3 = require("sqlite3").verbose();
const md5 = require("md5");
const DBSOURCE = "./express-sqlite/database.db";

const db = new sqlite3.Database(DBSOURCE, (err) => {
  if (err) {
    console.error('Error opening database:', err.message);
  } else {
    console.log('Connected to the database');

    // Create Leads table
    db.run(`CREATE TABLE IF NOT EXISTS Leads (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      leadName TEXT NOT NULL UNIQUE, 
      postCode INTEGER NOT NULL,
      data TEXT,
      state TEXT DEFAULT 'new',
      advisor INTEGER DEFAULT 'unassined',
      creationDate DATETIME DEFAULT CURRENT_TIMESTAMP, -- New column for creation date
      FOREIGN KEY(advisor) REFERENCES Advisor(advisorid)
    )`, (err) => {
      if (err) {
        console.error('Error creating Leads table:', err.message);
      } else {
        console.log('Leads table created successfully');
      }
    });

    // Create Advisor table
    db.run(`CREATE TABLE IF NOT EXISTS Advisor (
      advisorid INTEGER PRIMARY KEY AUTOINCREMENT,
      firstname TEXT NOT NULL,
      familyname TEXT NOT NULL, 
      email TEXT UNIQUE  NOT NULL,
      phone TEXT NOT NULL,
      ga TEXT NOT NULL,
      pwd TEXT NOT NULL
    )`, (err) => {
      if (err) {
        console.error('Error creating Advisor table:', err.message);
      } else {
        console.log('Advisor table created successfully');
      }
    });
  }
});

module.exports = {
  db
};
