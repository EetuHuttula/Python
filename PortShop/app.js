const config = require('./utils/config')
const express = require('express')
const cors = require('cors')
const app = express()
const middleware = require('./utils/middleware')
const logger = require('./utils/logger')
const mongoose = require('mongoose')

const productsRouter = require('./controllers/products')
const categoriesRouter = require('./controllers/categories')

mongoose.set('strictQuery', false)

logger.info('connecting to', config.MONGODB_URI)

mongoose.connect(config.MONGODB_URI)
  .then(() => {
    logger.info('connected to MongoDB')
  })
  .catch((error) => {
    logger.error('error connection to MongoDB:', error.message)
  })

app.use(cors())
app.use(express.static('dist'))
app.use(express.json())
app.use(middleware.requestLogger)

console.log('NODE_ENV:', process.env.NODE_ENV);
if (process.env.NODE_ENV === 'test') {
  const testingRouter = require('./controllers/tests') 
   app.use('/api/testing', testingRouter)
   console.log('Running in test environment');
  }

app.use('/api/products', productsRouter)
app.use('/api/categories', categoriesRouter);

app.use(middleware.unknownEndpoint)
app.use(middleware.errorHandler)

module.exports = app