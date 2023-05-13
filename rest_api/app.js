const { request } = require('express')
const express = require('express')
const app = express()
const database = require("./express-sqlite/database.js")
const bodyParser = require("body-parser")
const port = 3000
app.use(bodyParser.urlencoded({
  extended: false
}));
app.use(bodyParser.json());


app.get('/', (req, res) => {
  res.send('Hello World!')
})


app.get('/obj', (req, res) => {
  obj = {1:"Sancho",2:"Heaton",3:"Rashford"}
  const token = req.headers.authorization;
  console.log(token);
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



app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})


//http://localhost:3000/ sq

//CREATE TABLE Team (id INT, name TEXT, position TEXT);
//CREATE TABLE Team (id INTEGER  PRIMARY KEY AUTOINCREMENT , name TEXT, position TEXT);
//INSERT INTO Team (id, name, position) VALUES ("1","De Gea","Goalkeeper");
//INSERT INTO Team (name, position) VALUES ("De Gea","Goalkeeper");
//.save database.db
//.open database.db