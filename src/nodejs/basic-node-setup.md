## Basic node app setup

When setting up node there a just a few basic things. 
1. Make a directory by running code in desired directory `mkdir <name_of_project>`
2. Create initialize node modules with `npm init`
3. Install express and morgan. `npm install <package>`
4. Create your app.js file.
5. Now setup you initial file with 
```
const express= require('express')
const app = express()
const logger = require('morgan')
const port = process.env.port || '3001'

app.use(logger('tiny'))

app.listen(port, ()=>{
	console.log(`You are connected to port:${port}`)
	})
```
**------------------------------------------------------------------------------------------------------------------------------------------------------**