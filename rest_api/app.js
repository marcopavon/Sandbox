const express = require('express');
const cors = require('cors');
const bodyParser = require('body-parser');
const basicAuth = require('express-basic-auth');
const bcryptjs = require('bcryptjs');
const jwt = require('jsonwebtoken');
require('dotenv').config();

const app = express();
const database = require("./express-sqlite/database.js").db; // Import the db object
const fs = require('fs');
const path = require('path');
const PORT = process.env.PORT || 3000; // Use the port provided by Heroku or default to 3000

// Corrected order of imports
const { request } = require('express');

app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());


// Add CORS middleware

app.use(cors({
  origin: ['http://localhost:3000'], // Allow requests only from this origin
  methods: ['GET', 'POST','PUT','DELETE'], // Allow only specified HTTP methods
  //allowedHeaders: ['Content-Type', 'Authorization'], // Allow only specified headers
}));


// Serve static files from the 'public' directory
app.use(express.static('public'));

const data = {1:"De Gea",2:"Heaton",8:"Fernandes",10:"Rashford"}

// will be overwrittgen due to static -> folder public, where index.html refers to the route"/"
app.get('/', (req, res) => {
  const { method, url, headers } = req;

  // Create a string with HTML line breaks
  const responseString = `Hello World!<br>Method: ${method}<br>URL: ${url}<br>Headers: ${JSON.stringify(headers)}<br>Data: ${JSON.stringify(data)}`;

  for (const player in data){
    console.log(`Manchster United: ${data[player]}`);
  }

  // Set the content type to HTML
  res.set('Content-Type', 'text/html');

  res.send(responseString);
})

app.get('/obj', (req, res) => {
  obj = {1:"Sancho",2:"Heaton",3:"Rashford"}
  const token = req.headers.authorization;
  let headerInformation = req.headers;
  let bodyInformation = req.body;

  //Console Ouput for debug
  console.log(token);
  console.log(headerInformation);
  console.log(bodyInformation);

  //Send response
  res.send(obj[1])
})

app.get('/json', (req, res, next) => {
  console.log(typeof(res));
  res.json({ answer: 42, hello: 'world' });
})

app.get('/db', (req, res) => {
  const sql = "SELECT * FROM Team";
  const param = [];
  database.all(sql,param, (err,rows) => {
    if (err){
    res.status(400).json({"error": err.message});
    return
  }
    res.json({
      "message": "success",
      "data": rows
    })
  })
})

app.get('/join', (req, res) => {
  const sql = `
    SELECT Player.name AS playerName, Team.name AS teamName
    FROM Player
    JOIN Team
    ON Player.teamId = Team.id
  `;

  database.all(sql, [], (err, rows) => {
    if (err) {
      console.error('Error fetching joined data:', err.message);
      res.status(500).json({ "error": "Internal Server Error" });
      return;
    }

    res.json({
      "message": "success",
      "data": rows
    });
  });
});


app.get('/db-new', (req, res) => {
  database.serialize(() => {

    database.all('SELECT rowid AS id, info FROM lorem', (err, row) => {
      res.json({"data": row})
    })
  })
  
  database.close()
})


app.get('/users/:id', (req, res) => {
  const userId = req.params.id;
  res.send(`Details of user ${userId}`);
});

app.get('/query', (req, res) => {
  //print all Queries
  console.log(req.query);

  const source = req.query.utm_source;
  res.send(`Used this parameters: ${source}`);
});

app.post('/post', (req, res) => {

  const data = {
    name : req.body.name,
    position : req.body.position
  }

  const sql = "INSERT INTO Team (name, position) VALUES (?,?)";
  const param = [data.name,data.position];

  database.run(sql,param, function(err, result){
    if (err){
      res.status(400).json({"error": err.message});
      return;
    }
    console.log(data);
    res.json({
      "messages" : "success",
      "data" : data,
      "id": this.lastID
    })
  })
})
 
app.post('/post-player', (req, res) => {
  const data = {
    name: req.body.name,
    teamId: req.body.teamId
  };

  const sql = "INSERT INTO Player (name, teamId) VALUES (?, ?)";
  const params = [data.name, data.teamId];

  database.run(sql, params, function (err, result) {
    if (err) {
      // Check for the unique constraint violation error
      if (err.message.includes('UNIQUE constraint failed')) {
        console.error('Error: Duplicate entry for unique constraint');
        res.status(409).json({ "error": "Duplicate entry" });
      } else {
        console.error('Error inserting into Player table:', err.message);
        res.status(400).json({ "error": err.message });
      }
      return;
    }

    console.log(data);
    res.json({
      "message": "success",
      "data": data,
      "id": this.lastID
    });
  });
});

app.patch('/update', (req, res) => {

  const data = {
    id : req.body.id,
    name : req.body.name,
    position : req.body.position
  }

  const sql = "UPDATE Team SET name=?, position=? WHERE id=?";
  const param = [data.name,data.position,data.id];

  database.run(sql,param, function(err, result){
    if (err){
      res.status(400).json({"error": err.message});
      return;
    }
    console.log(data);
    res.json({
      "messages" : "successful updated",
      "data" : data,
      "id": this.lastID
    })
  })
})

// Dummy database
const users = [

];


// Register route
app.post('/register', async (req, res) => {
  try {
      const hashedPassword = await bcryptjs.hash(req.body.password, 10);
      const user = { username: req.body.username, password: hashedPassword };
      users.push(user);
      res.status(201).send('User registered successfully');
  } catch {
      res.status(500).send('Failed to register user');
  }
});

// Login route
app.post('/login', async (req, res) => {
  try {
    const user = users.find(user => user.username === req.body.username);
    if (!user) {
      return res.status(400).send('User not found');
    }

    const passwordMatch = await bcryptjs.compare(req.body.password, user.password);
    if (!passwordMatch) {
      return res.status(401).send('Invalid password');
    }

    const accessToken = jwt.sign({
      username: user.username,
      test: "test",
      role: "admin"
    }, process.env.JWT_SECRET);
    res.json({ accessToken: accessToken });
  } catch (error) {
    console.error('Login error:', error);
    res.status(500).send('Internal Server Error');
  }
});

// Protected route
app.get('/protected', authenticateToken, (req, res) => {
  console.log(req.user);

  database.all("SELECT * FROM Leads WHERE id = ?", [1], (err, rows) => {
    if (err) {
      return res.status(500).send('Error fetching leads: ' + err.message);
    } else {
      console.log(rows);
      res.send('Protected route accessed');
    }
  }); // <-- Missing closing parenthesis here
});

// GET endpoint to verify JWT token
app.get('/verify-token/:token', (req, res) => {
  const token = req.params.token; // Get token from URL parameter
  console.log(token)
  try {
    // Verify the token
    const decoded = jwt.verify(token, process.env.JWT_SECRET);
    res.json({ valid: true, decoded: decoded });
  } catch (error) {
    res.status(401).json({ valid: false, error: error.message });
  } 
});









  // Endpoint to handle POST request for a new lead
  app.post('/advisor-register', async (req, res) => {
    console.log("Received body in backend: ", req.body);
    const { firstname, familyname, email, phone, ga, pwd } = req.body;
  
    // Input Validation
    if (!email || !firstname || !familyname || !phone || !ga || !pwd) {
      return res.status(400).send({ error: 'All fields are required' });
    }
  
    try {
      // Hash the password
      const hashedPassword = await bcryptjs.hash(pwd, 10);
  
      // Check if advisor with the same firstname and familyname already exists
      const checkSql = `SELECT * FROM Advisor WHERE email = ?`;
      database.get(checkSql, [email], (err, row) => {
        if (err) {
          console.error('Failed to execute query:', err.message);
          return res.status(500).send({ error: 'Failed to execute query' });
        }
        if (row) {
          // Advisor with the same firstname and familyname already exists
          return res.status(409).send({ error: 'Advisor with the given names already exists' });
        } else {
          // Advisor does not exist, proceed with insertion
          const insertSql = `INSERT INTO Advisor (firstname, familyname, email, phone, ga, pwd) VALUES (?, ?, ?, ?, ?, ?)`;
          database.run(insertSql, [firstname, familyname, email, phone, ga, hashedPassword], function (insertErr) {
            if (insertErr) {
              console.error('Failed to add new advisor:', insertErr.message);
              return res.status(500).send({ error: 'Failed to add new advisor' });
            }
            // Return the ID of the newly created advisor
            res.status(201).send({ id: this.lastID });
          });
        }
      });
    } catch (error) {
      console.error('Error while processing request:', error);
      res.status(500).send({ error: 'Internal Server Error' });
    }
  });

  app.post('/advisor-login', async (req, res) => {
    try {
      const { email, pwd } = req.body;
      console.log(req.body);
  
      // Input Validation
      if (!email || !pwd) {
        return res.status(400).send({ error: 'Email and password are required' });
      }
  
      // Check if advisor with the given email exists
      const checkSql = `SELECT * FROM Advisor WHERE email = ?`;
      database.get(checkSql, [email], async (err, row) => {
        if (err) {
          console.error('Failed to execute query:', err.message);
          return res.status(500).send({ error: 'Failed to execute query' });
        }
  
        // If advisor not found
        if (!row) {
          return res.status(400).send({ error: 'Advisor not found' });
        }
  
        // Compare passwords
        const passwordMatch = await bcryptjs.compare(pwd, row.pwd);
        if (!passwordMatch) {
          return res.status(401).send({ error: 'Invalid password' });
        }
         
        // Generate JWT token
        const accessToken = jwt.sign({
          advisorid: row.advisorid,
          email: row.email
        }, process.env.JWT_SECRET);
  
        // Respond with access token
        res.json({ accessToken: accessToken });
      });
    } catch (error) {
      console.error('Login error:', error);
      res.status(500).send({ error: 'Internal Server Error' });
    }
  });

  app.get('/advisor-data', authenticateToken, (req, res) => {
    console.log(req.user);   

    database.all("SELECT * FROM Leads JOIN Advisor ON Leads.advisor = Advisor.advisorid WHERE Advisor.advisorid = ?", [req.user.advisorid], (err, rows) => {
        if (err) {
            return res.status(500).send('Error fetching leads: ' + err.message);
        } else {
            console.log(rows);
            // Set content type header to indicate JSON response
            res.setHeader('Content-Type', 'application/json');
            res.send(JSON.stringify(rows)); // Send JSON response
        }
    }); 
});


// Middleware to authenticate tokens
function authenticateToken(req, res, next) {
  const token = req.headers['authorization'];
  console.log(`Inside Middleware: ${token}`);
  
  if (!token) {
      return res.status(401).send('Access Denied');
  }

  jwt.verify(token, process.env.JWT_SECRET, (err, user) => {
  //console.log(user)
      if (err) {
          //console.log(token, process.env.JWT_SECRET);
          console.error('JWT Verification Error:', err.message);
          // Additional error handling based on the type of error
          if (err.name === 'TokenExpiredError') {
              return res.status(401).send('Token Expired');
          } else if (err.name === 'JsonWebTokenError' || err.name === 'SyntaxError') {
              return res.status(403).send('Invalid Token');
          } else {
              return res.status(500).send('Internal Server Error');
          }
      }
      
      // Authentication successful, attach user information to request object
      console.log(`Auth Service: Successful with user: ${JSON.stringify(user, null, 2)}`);
      req.user = user;
      next();
  });
}


  
// Define valid credentials
const validUsers = { 'test': '1234' };

// Middleware to check Basic Authentication credentials
const checkCredentials = (username, password) => {
    return validUsers[username] && validUsers[username] === password;
};


// Endpoint to handle POST request for a new lead
app.post('/leads', (req, res) => {
  console.log(req.body);
  const { leadName, postCode, data } = req.body;

  // Server-side validation for postcode
  if (!/^\d{4}$/.test(postCode)) {
    return res.status(400).send('Invalid postcode. Postcode must be exactly 4 digits.');
  }

  // SQL query to insert a new lead
  const sql = `INSERT INTO Leads (leadName, postCode, data) VALUES (?, ?, ?)`;
  database.run(sql, [leadName, postCode, data], function(err) {
      if (err) {
          res.status(500).send('Error saving the lead: ' + err.message);
      } else {
          res.send(`Lead with ID ${this.lastID} created successfully`);
      }
  });
});



// Route to get all leads
app.get('/leads', (req, res) => {
  console.log(req.originalUrl);

  database.all("SELECT * FROM Leads", [], (err, rows) => {
      if (err) {
          res.status(500).send('Error fetching leads: ' + err.message);
      } else {
          // Extract the token from the Authorization header
          const token = req.headers.authorization;
          console.log(`Token is: ${token}`);
          console.log(req.headers);
          res.json(rows);
      }
  });
});

// Route to get all leads
app.get('/leads-auth', basicAuth({
  authorizer: checkCredentials,
  unauthorizedResponse: (req) => {
      return 'Unauthorized';
  }
}), (req, res) => {
  console.log(req.originalUrl);

  database.all("SELECT * FROM Leads", [], (err, rows) => {
      if (err) {
          res.status(500).send('Error fetching leads: ' + err.message);
      } else {
          // Extract the token from the Authorization header
          const token = req.headers.authorization;
          console.log(`Token is: ${token}`);
          //Whats the output from the query
          console.log(rows);
          res.json(rows);
      }
  });
});

// Route to get one specific
app.get('/get-lead-by-id/:id', (req, res) => {
  const id = req.params.id;
    // Assuming 'advisor_id' is the foreign key in 'Leads' table that references 'id' in 'Advisor' table
    const sql = `
    SELECT
      *
    FROM 
        Leads 
    LEFT JOIN 
        Advisor
    ON Leads.advisor = Advisor.advisorid
    WHERE
    Leads.id = ?

`;
  // Need Left join, cause un assined is not in Advisory Table
  database.all(sql, [id], (err, rows) => {
    if (err) {
      console.error(err.message);
      res.status(500).json({ error: 'Error fetching lead details' });
      return;
  }
  console.log("body from resp.:",rows);

  res.json(rows);
});
});


// Route to get all leads
app.get('/advisors', (req, res) => {
  database.all("SELECT * FROM Advisor", [], (err, rows) => {
      if (err) {
          res.status(500).send('Error fetching leads: ' + err.message);
      } else {
          console.log(rows);
          res.json(rows);
      }
  });
});


//get all postCodes inside the Database to populate the Dropdown for the filter
app.get('/postcodes', (req, res) => {
  const sql = "SELECT DISTINCT postCode FROM Leads";
  database.all(sql, [], (err, rows) => {
      if (err) {
          console.error(err);
          res.status(500).send('Error fetching postcodes');
      } else {
          const uniquePostcodes = rows.map(row => row.postCode);
          res.json(uniquePostcodes);
      }
  });
});

// Delete entry on Dashboard based on button click.
app.delete('/leads/:id', (req, res) => {
  const id = req.params.id;
  const sql = 'DELETE FROM Leads WHERE id = ?';

  database.run(sql, id, function(err) {
      if (err) {
          res.status(500).json({ error: err.message });
          return;
      }
      res.json({ message: `Lead with ID ${id} was deleted`, changes: this.changes });
  });
});



//Update leads based on changes from the Dashboard
app.post('/update-lead-state', (req, res) => {
  console.log(req.body);
  const { state, id } = req.body;
  // Update the lead state in the database
  const sql = `UPDATE Leads SET state = ? WHERE id = ?`;
  database.run(sql, [state, id], function(err) {
    if (err) {
      res.status(500).send({ message: "Error updating lead state", error: err.message });
    } else {
      res.send({ message: "Lead state updated successfully" });
    }
  });
});

// Update advisor based on changes from the Dashboard
app.post('/update-advisor-dashboard', (req, res) => {
  console.log(req.body);
  const { advisor, id } = req.body;
  // This assumes the 'advisor' field correctly matches the advisor ID or name in your Leads table
  const sql = `UPDATE Leads SET advisor = ? WHERE id = ?`;

  database.run(sql, [advisor, id], function(err) {
    if (err) {
      // Updated error message to reflect the operation being performed
      res.status(500).send({ message: "Error updating advisor for the lead", error: err.message });
    } else {
      // Updated success message for clarity
      res.send({ message: "Advisor updated successfully for the lead" });
    }
  });
});

//Get all postcodes from a lookup
app.get('/api/postcode-lookup', async (req, res) => {
  try {
      // Construct a path relative to this script's location
      const filePath = path.join(__dirname, 'postcodeLookup.json');
      const data = JSON.parse(fs.readFileSync(filePath, 'utf8'));
      res.json(data);
  } catch (error) {
      console.error(error); // Log the error for debugging
      res.status(500).send('Error reading postcode lookup data');
  }
});

// changeds in db sometimes needs to drop the old one
//database.run(`DROP TABLE IF EXISTS Leads`);
//database.run(`DROP TABLE IF EXISTS Advisor`);
//database.run("ALTER TABLE Leads ADD COLUMN advisor TEXT DEFAULT 'none'");

//database.run("ALTER TABLE Leads ADD COLUMN creationDate DATETIME");
//database.run('UPDATE Leads SET creationDate = NULL');



/*
// Check if the Team table exists
database.run(`
  CREATE TABLE IF NOT EXISTS Team (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
  )
`, (err) => {
  if (err) {
    console.error('Error creating Team table:', err.message);
  } else {
    console.log('Team table created successfully');

  // Now, create the Player table with a foreign key reference to the Team table
  database.run(`
  CREATE TABLE IF NOT EXISTS Player (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    teamId INTEGER,
    FOREIGN KEY (teamId) REFERENCES Team(id)
  )
    `, (err) => {
      if (err) {
        console.error('Error creating Player table:', err.message);
      } else {
        console.log('Player table created successfully');
      }
    });
  }
});
*/





app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});

