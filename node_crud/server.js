require('./models/db')

const path = require('path')
const express = require('express')
const employeeController = require('./controllers/employeeController')
const exphbs = require('express-handlebars')
const bodyparser = require('body-parser')

let app = express()

app.use(bodyparser.urlencoded({
    extended: true
}))
app.use(bodyparser.json())
app.set('views',path.join(__dirname,'/views/'))
app.engine('hbs',exphbs({extname: 'hbs',defaultLayout: 'mainLayout', layoutsDir: __dirname+ '/views/layouts/'}))
app.set('view engine','hbs')

app.listen(3000, ()=>{
    console.log('Express Server started at localhost/3000')
})
app.use('/employee',employeeController)