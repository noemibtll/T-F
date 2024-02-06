import fs from 'fs';
const checkpointPath = "src/state.json";

const getCheckpoint = () => {
    const state = fs.readFileSync(checkpointPath);
    return JSON.parse(state);
}

const setCheckpoint = (data) => {
    fs.writeFileSync(checkpointPath, JSON.stringify(data, null, 4));
}

const cleanCheckpoint = (checkpoint) => {
    fs.writeFileSync(checkpointPath, JSON.stringify({
        "checkpoint": checkpoint,
        "word_idx": 0,
        "paragraph_status": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    }, null, 4));
}

export default {getCheckpoint, setCheckpoint, cleanCheckpoint}