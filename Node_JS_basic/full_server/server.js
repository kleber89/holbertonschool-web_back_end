import express from 'express';
import routes from './routes/index';

const app = express();
const port = 1245;

// Use the defined routes
app.use('/', routes);

// Start the server
app.listen(port, () => {
  console.log(`Server running on port ${port}`);
});

export default app;