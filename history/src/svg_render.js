// Clear SVG element
function clearSVG() {
  svgElement.innerHTML = '';
}

// Draw time ranges
function drawTimeRanges(timeRanges, margin, height, yearScale) {
  // First, we need to calculate the rightmost position for each parent event
  // to properly set the width of the parent rectangle
  const parentWidthMap = new Map();

  // Calculate the required width for each parent based on its children
  timeRanges.forEach(event => {
    let rightmostX = event.x; // Start with parent's own x position

    // Find all children of this event
    const children = timeRanges.filter(child =>
      child.parents &&
      child.parents.length > 0 &&
      child.parents[0] === event.key
    );

    // Find max x position among children
    children.forEach(child => {
      rightmostX = Math.max(rightmostX, child.x);
    });

    // Store the rightmost position for this parent
    parentWidthMap.set(event.key, rightmostX);
  });

  timeRanges.forEach((event) => {
    const x = event.x;

    if (event.startY >= margin.top && event.startY <= height - margin.bottom) {
      // For time ranges, draw a rectangle
      const rectHeight = Math.abs(event.endY - event.startY);
      const rectY = Math.min(event.startY, event.endY);

      // Determine the width of the rectangle based on whether this is a parent
      let rectWidth = 24; // Default width
      let rectX = x - 8;  // Default x position

      // Check if this event has children and adjust width accordingly
      const rightmostX = parentWidthMap.get(event.key);
      if (rightmostX && rightmostX > event.x) {
        // This event is a parent, expand its rectangle to cover its children
        rectX = x - 8; // Left edge at parent's position
        rectWidth = (rightmostX - x) + 24; // Width to cover up to rightmost child
      } else {
        // Regular event with default width
        rectX = x - 8;
        rectWidth = 24;
      }

      // Generate softer color for time range rectangle
      const fillColor = getSoftColor();

      // Time range rectangle
      const rangeRect = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
      rangeRect.setAttribute('x', rectX);
      rangeRect.setAttribute('y', rectY);
      rangeRect.setAttribute('width', rectWidth);
      rangeRect.setAttribute('height', rectHeight);
      rangeRect.setAttribute('fill', fillColor);
      rangeRect.setAttribute('stroke', 'transparent');
      rangeRect.setAttribute('stroke-width', 1);
      rangeRect.setAttribute('rx', 8);
      rangeRect.setAttribute('ry', 8);
      rangeRect.setAttribute('class', 'timeline-range');
      svgElement.appendChild(rangeRect);
    }
  });
}

// Draw single points
function drawSinglePoints(singlePoints, margin, height) {
  singlePoints.forEach((event) => {
    const x = event.x;

    if (event.startY >= margin.top && event.startY <= height - margin.bottom) {
      // Draw event connector line
      const connector = document.createElementNS('http://www.w3.org/2000/svg', 'line');
      connector.setAttribute('x1', margin.left);
      connector.setAttribute('y1', event.startY);
      connector.setAttribute('x2', x - 15);
      connector.setAttribute('y2', event.startY);
      connector.setAttribute('stroke', '#c5d0e6');
      connector.setAttribute('stroke-width', 2);
      connector.setAttribute('stroke-dasharray', '6,4');
      svgElement.appendChild(connector);

      // Draw event dot
      const marker = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
      marker.setAttribute('cx', x);
      marker.setAttribute('cy', event.startY);
      marker.setAttribute('r', 8);
      marker.setAttribute('class', 'timeline-marker');
      svgElement.appendChild(marker);
    }
  });
}