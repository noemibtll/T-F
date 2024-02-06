import express from 'express';
import path from 'path';
import Checkpoint from './checkpoint.js';

const __dirname = path.resolve();
const app = express();
app.use(express.urlencoded({ extended: true }));
app.use(express.json());

const words = ["Rust", "is", "blazingly", "fast", "and", "memory-efficient:", "with", "no", "runtime", "or", "garbage", "collector,", "it", "can", "power", "performance-critical", "services,", "run", "on", "embedded", "devices,", "and", "easily", "integrate", "with", "other", "languages."];

app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'src/views/index.html'))
});


app.get('/restart', (req, res) => {
    const checkpoint = Date.now();
    Checkpoint.cleanCheckpoint(checkpoint);
    res.json({"get": true, "checkpoint": checkpoint});
});
app.get('/word', (req, res) => {
    res.json({
        ...Checkpoint.getCheckpoint(),
        "paragraph": words
    });
});
app.post('/word', (req, res) => {
    const { word_idx, paragraph_status } = req.body;
    const checkpoint = Date.now();
    Checkpoint.setCheckpoint({
        "word_idx": parseInt(word_idx),
        "paragraph_status": paragraph_status,
        "checkpoint": checkpoint
    });
    res.json({"post": true, "checkpoint": checkpoint});
});


app.listen(3000);