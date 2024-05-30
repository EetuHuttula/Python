const productsRouter = require('express').Router()
const Product = require('../models/product')
const Category = require('../models/category')

productsRouter.get('/', async (request, response) => {
    try {
      const products = await Product.find({}).populate('category', { name: 1, description: 1 });
      response.json(products);
    } catch (error) {
      response.status(500).json({ error: 'Failed to fetch products' });
    }
  });

productsRouter.get('/:id', async (request, response, next) => {
    try {
        const product = await Product.findById(request.params.id).populate('category', { name: 1, description: 1 });
        if (product) {
        response.json(product);
        } else {
        response.status(404).end();
        }
    } catch (error) {
        next(error);
    }
});

productsRouter.post('/', async (request, response, next) => {
    const body = request.body;
  
    try {
      const category = await Category.findById(body.category);
      if (!category) {
        return response.status(400).json({ error: 'Invalid category' });
      }
  
      if (!body.name) {
        return response.status(400).json({ error: 'Name is required' });
      }
      if (!body.price) {
        return response.status(400).json({ error: 'Price is required' });
      }
  
      const product = new Product({
        name: body.name,
        description: body.description,
        price: body.price,
        category: body.category,
        created_at: new Date(),
        updated_at: new Date()
      });
  
      const savedProduct = await product.save();
      response.status(201).json(savedProduct);
    } catch (error) {
      next(error);
    }
  });
  
  productsRouter.put('/:id', async (request, response, next) => {
    const body = request.body;
  
    const product = {
      name: body.name,
      description: body.description,
      price: body.price,
      category: body.category,
      updated_at: new Date()
    };
  
    try {
      const updatedProduct = await Product.findByIdAndUpdate(request.params.id, product, { new: true });
      response.json(updatedProduct);
    } catch (error) {
      next(error);
    }
  });
  
  module.exports = productsRouter;