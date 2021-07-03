//Server script using Express framework
const express = require('express');

const server = express();

//Server response to any request
server.all('/', (req, res) =>{
  res.send("The Professor is online.")
})

//Start the server
function keepOnline(){
  server.listen(3000, ()=>{console.log("Server is online.")});
}

module.exports = keepOnline;