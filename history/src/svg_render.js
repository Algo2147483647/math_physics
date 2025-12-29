// Clear SVG element
function clearSVG() {
  svgElement.innerHTML = '';
}

// Draw time ranges
function drawTimeRanges(timeRanges, margin, height, yearScale) {
  widthUnit = window.horizontalScaleValue; // Use global horizontal scale variable from app.js

  timeRanges.forEach((event) => {
    if (event.startY >= margin.top && event.startY <= height - margin.bottom) {
      // Time range rectangle
      const rangeRect = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
      rangeRect.setAttribute('x', event.x * widthUnit + margin.left + 4);
      rangeRect.setAttribute('y', Math.min(event.startY, event.endY));
      rangeRect.setAttribute('width', event.width * widthUnit - 4);
      rangeRect.setAttribute('height', Math.abs(event.endY - event.startY));
      rangeRect.setAttribute('fill', getRandomColor(event.x, event.width));
      rangeRect.setAttribute('stroke', 'transparent');
      rangeRect.setAttribute('stroke-width', 1);
      rangeRect.setAttribute('rx', 8);
      rangeRect.setAttribute('ry', 8);
      rangeRect.setAttribute('class', 'timeline-range');
      
      // Add event listeners for hover
      rangeRect.addEventListener('mouseenter', (e) => {
        showEventCard(event, e.clientX, e.clientY);
      });
      
      rangeRect.addEventListener('mouseleave', () => {
        hideEventCard();
      });
      
      rangeRect.addEventListener('mousemove', (e) => {
        updateEventCardPosition(e.clientX, e.clientY);
      });
      
      svgElement.appendChild(rangeRect);
    }
  });
}

// Draw single points
function drawSinglePoints(singlePoints, margin, height) {
  widthUnit = window.horizontalScaleValue; // Use global horizontal scale variable from app.js

  // First, draw all connector lines (dashed lines)
  singlePoints.forEach((event) => {
    const x = event.x * widthUnit + margin.left + 16;

    if (event.startY >= margin.top && event.startY <= height - margin.bottom) {
      // Draw event connector line
      const connector = document.createElementNS('http://www.w3.org/2000/svg', 'line');
      connector.setAttribute('x1', margin.left);
      connector.setAttribute('y1', event.startY);
      connector.setAttribute('x2', x);
      connector.setAttribute('y2', event.startY);
      connector.setAttribute('stroke', '#c5d0e6');
      connector.setAttribute('stroke-width', 2);
      connector.setAttribute('stroke-dasharray', '6,4');
      svgElement.appendChild(connector);
    }
  });

  // Then, draw all event dots on top
  singlePoints.forEach((event) => {
    const x = event.x * widthUnit + margin.left + 16;

    if (event.startY >= margin.top && event.startY <= height - margin.bottom) {
      // Draw event dot
      const marker = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
      marker.setAttribute('cx', x);
      marker.setAttribute('cy', event.startY);
      marker.setAttribute('r', 8);
      marker.setAttribute('class', 'timeline-marker');
      
      // Add event listeners for hover
      marker.addEventListener('mouseenter', (e) => {
        showEventCard(event, e.clientX, e.clientY);
      });
      
      marker.addEventListener('mouseleave', () => {
        hideEventCard();
      });
      
      marker.addEventListener('mousemove', (e) => {
        updateEventCardPosition(e.clientX, e.clientY);
      });
      
      svgElement.appendChild(marker);
    }
  });
}