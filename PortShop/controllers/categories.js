const categoriesRouter = require('express').Router();
const Category = require('../models/category'); 

categoriesRouter.get('/', async (request, response) => {
  try {
    const categories = await Category.find({});
    response.json(categories);
  } catch (error) {
    response.status(500).json({ error: 'Failed to fetch categories' });
  }
});

categoriesRouter.get('/:id', async (request, response, next) => {
  try {
    const category = await Category.findById(request.params.id);
    if (category) {
      response.json(category);
    } else {
      response.status(404).end();
    }
  } catch (error) {
    next(error);
  }
});

categoriesRouter.post('/', async (request, response, next) => {
  const body = request.body;

  if (!body.name) {
    return response.status(400).json({ error: 'Name is required' });
  }

  const category = new Category({
    name: body.name,
    description: body.description,
    created_at: new Date(),
    updated_at: new Date()
  });

  try {
    const savedCategory = await category.save();
    response.status(201).json(savedCategory);
  } catch (error) {
    next(error);
  }
});

categoriesRouter.delete('/:id', async (request, response, next) => {
  try {
    await Category.findByIdAndDelete(request.params.id);
    response.status(204).end();
  } catch (error) {
    next(error);
  }
});


categoriesRouter.put('/:id', async (request, response, next) => {
  const body = request.body;

  const category = {
    name: body.name,
    description: body.description,
    updated_at: new Date()
  };

  try {
    const updatedCategory = await Category.findByIdAndUpdate(request.params.id, category, { new: true });
    response.json(updatedCategory);
  } catch (error) {
    next(error);
  }
});

module.exports = categoriesRouter;
