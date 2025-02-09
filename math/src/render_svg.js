function render_file_graph(path, root) {
    request("build_graph_json_from_markdown_folder", {"folder_path": path}).then(dag => {
        console.log(dag);
        RenderSvgFromDag(dag, root)
    })
    .catch(error => {
        console.error('Error fetching file graph:', error); // 捕获错误
    });
}

function RenderSvgFromDag(dag, root) {
    container = document.getElementById('main-content');
    if (container) {
        container.parentNode.removeChild(container);
    }
    container = document.createElement('div');
    container.id = 'main-content';
    document.body.appendChild(container);

    const svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
    svg.setAttribute("width", "10000");
    svg.setAttribute("height", "10000");
    container.appendChild(svg);


    for (const key in dag) {
        if (dag.hasOwnProperty(key)) {
            const item = dag[key];
            if (item.hasOwnProperty('coordinate')) {
                delete item.coordinate;
            }
        }
    }
    BuildCoordinateForDag(dag, root)
    RenderNodeCoordinate(dag)
    RenderByDFS(dag, svg, root, new Set());

    // 自动导出 SVG 文件
    // const svgData = new XMLSerializer().serializeToString(svg);
    // const blob = new Blob([svgData], { type: 'image/svg+xml' });
    // const url = URL.createObjectURL(blob);
    // const a = document.createElement('a');
    // a.href = url;
    // a.download = 'math.svg';
    // a.click();
    // URL.revokeObjectURL(url);
}

function RenderNodeCoordinate(dag) {
    let elements_num = Array(100).fill(0);
    for (let key in dag) {
        if (!dag[key].hasOwnProperty('coordinate')) {
            continue
        }

        let coordinate = dag[key]["coordinate"];
        elements_num[coordinate[0]] = Math.max(elements_num[coordinate[0]], coordinate[1] + 1);
    }

    let elements_num_max = Math.max(...elements_num);
    for (let key in dag) {
        if (!dag[key].hasOwnProperty('coordinate')) {
            continue
        }

        let coordinate = dag[key]["coordinate"];
        dag[key]["coordinate_SVG"] = coordinate;
        dag[key]["coordinate_SVG"][1] = (elements_num_max * 50) / elements_num[coordinate[0]] * (coordinate[1] + 0.5);
        dag[key]["coordinate_SVG"][0] = (coordinate[0] + 1) * 300 - 200;
    }
}

function RenderByDFS(dag, svg, nodeKey, visited) {
    visited.add(nodeKey);
    dag[nodeKey]["kids"].forEach(kidKey => {
        const radius = 8;
        RenderEdge(svg,
            dag[nodeKey]["coordinate_SVG"][0] + radius, dag[nodeKey]["coordinate_SVG"][1],
            dag[kidKey] ["coordinate_SVG"][0] - radius, dag[kidKey] ["coordinate_SVG"][1]);

        if (!visited.has(kidKey)) {
            RenderByDFS(dag, svg, kidKey, visited);
        }
    });

    [x, y] = dag[nodeKey]["coordinate_SVG"];
    RenderNode(dag, svg, x, y, nodeKey);
}

function RenderNode(dag, svg, x, y, nodeKey) {
    const radius = 8;
    const circle = document.createElementNS("http://www.w3.org/2000/svg", "circle");
    circle.setAttribute("cx", x);
    circle.setAttribute("cy", y);
    circle.setAttribute("r", radius);
    circle.setAttribute("stroke", "#FF6347"); // Tomato color for stroke
    circle.setAttribute("fill", "#FFB6C1"); // Light pink for fill
    circle.setAttribute("stroke-width", "2");

    const text = document.createElementNS("http://www.w3.org/2000/svg", "text");
    text.setAttribute("x", x + radius * 1.5);
    text.setAttribute("y", y + radius / 1.25);
    text.setAttribute("font-family", "Georgia, serif"); // More elegant font
    text.setAttribute("font-style", "italic"); // Italicize the text
    text.setAttribute("font-size", "16");
    text.setAttribute("fill", "#333"); // Darker color for text
    text.textContent = nodeKey.split('\\').pop().split('.')[0].replace(/_/g, ' ');

    const circleLink = document.createElementNS("http://www.w3.org/2000/svg", "a");
    circleLink.setAttribute("href", "javascript:void(0)");  // You can use this to prevent default link action
    circleLink.addEventListener('click', () => render_file_graph("C:/Algo/Notes/math_physics/math/", nodeKey));

    const textLink = document.createElementNS("http://www.w3.org/2000/svg", "a");
    textLink.setAttribute("href", "javascript:void(0)");
    textLink.setAttribute("target", "_blank");
    textLink.addEventListener('click', () => request("open_typora", {path: "C:/Algo/Notes/math_physics/math/" + nodeKey + ".md"}));

    circleLink.appendChild(circle);
    textLink.appendChild(text);
    svg.appendChild(circleLink);
    svg.appendChild(textLink);
}

function RenderEdge(svg, x1, y1, x2, y2) {
    const path = document.createElementNS("http://www.w3.org/2000/svg", "path");
    const d = `M ${x1} ${y1} C ${(x1 + x2) / 2} ${y1} ${(x1 + x2) / 2} ${y2} ${x2} ${y2}`;

    path.setAttribute("d", d);
    path.setAttribute("stroke", "#8888FF");
    path.setAttribute("fill", "none");
    path.setAttribute("stroke-width", "1");
    svg.appendChild(path);
}
