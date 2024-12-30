//import fetch from "node-fetch";
// Used for Browser Script

const urlTest = "https://catfact.ninja/fact";

//ajax 
async function getData (api){
    const response = await fetch(api);
    var data = await response.json();
    //console.log("1st function");
    console.log(data["fact"])
    return data
    }


getData(urlTest)

console.log("########");

//get request
const url = "https://jsonplaceholder.typicode.com/posts/1";


fetch(url).then((response)=>{
  return response.json();  // converting byte data to json
}).then(data=>{
  console.log(data)
});

//post request

/* const params = {
    param1: 1,
    param2: 2 
};
const options = {
    method: 'POST',
    body: JSON.stringify( params )  
};
fetch( 'https://reqres.in/api/users/path/', options )
    .then( response => response.json() )
    .then( response => {
        console.log(options)
        console.log("post send")
    } ); */