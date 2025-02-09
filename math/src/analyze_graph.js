function FindRootsFromDag() {
    const allNodes = new Set(Object.keys(dag));
    for (let nodeName in dag) {
        for (let kid of dag[nodeName].kid) {
            allNodes.delete(kid);
        }
    }
    return Array.from(allNodes);
}

function BuildCoordinateForDag(dag, root) {
    const queue = [root];
    let level = -1;

    while (queue.length) {
        const n = queue.length;
        level += 1;
        for (let i = 0; i < n; i++) {
            const key = queue.shift();
            dag[key]["coordinate"] = [level, i];
            dag[key].kids.forEach(kidKey => {
                if (!dag[kidKey].hasOwnProperty('coordinate')) {
                    queue.push(kidKey);
                    dag[kidKey]["coordinate"] = [-1, -1];
                }
            });
        }
    }

    return dag;
}
