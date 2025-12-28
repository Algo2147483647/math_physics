// Clear SVG element
function clearSVG() {
  svgElement.innerHTML = '';
}

// Create event card SVG group
function createEventCard(event, x, y, isTimeRange = false) {
  const cardGroup = document.createElementNS('http://www.w3.org/2000/svg', 'g');
  cardGroup.setAttribute('class', 'event-card');
  cardGroup.addEventListener('click', () => showEventDetails(event));

  // Card background (initially hidden)
  const cardBg = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
  cardBg.setAttribute('x', x + 20);
  cardBg.setAttribute('y', y - 30);
  cardBg.setAttribute('width', 200);
  cardBg.setAttribute('height', 60);
  cardBg.setAttribute('rx', 8);
  cardBg.setAttribute('ry', 8);
  cardBg.setAttribute('fill', 'white');
  cardBg.setAttribute('stroke', '#e0e0e0');
  cardBg.setAttribute('stroke-width', 1);
  cardBg.setAttribute('class', 'event-card-bg');
  cardBg.style.display = 'none'; // Initially hidden
  cardGroup.appendChild(cardBg);

  // Event title (always visible)
  const title = document.createElementNS('http://www.w3.org/2000/svg', 'text');
  title.setAttribute('x', x + 120);
  title.setAttribute('y', y - 15);
  title.setAttribute('text-anchor', 'middle');
  title.setAttribute('class', 'event-title');
  title.textContent = truncateText(event.key || 'N/A', 25);
  cardGroup.appendChild(title);

  // Year label (initially hidden)
  const yearLabel = document.createElementNS('http://www.w3.org/2000/svg', 'text');
  yearLabel.setAttribute('x', x + 120);
  yearLabel.setAttribute('y', y + 5);
  yearLabel.setAttribute('text-anchor', 'middle');
  yearLabel.setAttribute('class', 'event-year');
  yearLabel.style.display = 'none'; // Initially hidden

  let yearDisplay;
  if (isTimeRange) {
    yearDisplay = event.startTime < 0 ? '-' + Math.abs(event.startTime) + ' - ' + (event.endTime < 0 ? '-' + Math.abs(event.endTime) : '+' + event.endTime) : '+' + event.startTime + ' - ' + (event.endTime < 0 ? '-' + Math.abs(event.endTime) : '+' + event.endTime);
  } else {
    yearDisplay = event.startTime < 0 ? '-' + Math.abs(event.startTime) : '+' + event.startTime;
  }
  yearLabel.textContent = yearDisplay;
  cardGroup.appendChild(yearLabel);

  // Person information (initially hidden)
  let personsElement = null;
  if (event.data.persons) {
    personsElement = document.createElementNS('http://www.w3.org/2000/svg', 'text');
    personsElement.setAttribute('x', x + 120);
    personsElement.setAttribute('y', y + 20);
    personsElement.setAttribute('text-anchor', 'middle');
    personsElement.setAttribute('class', 'event-persons');
    personsElement.style.display = 'none'; // Initially hidden
    personsElement.textContent = truncateText(Array.isArray(event.data.persons) ? event.data.persons.join(', ') : event.data.persons, 25);
    cardGroup.appendChild(personsElement);
  }

  // Add event listeners for hover effect
  cardGroup.addEventListener('mouseenter', () => {
    // Show all elements
    cardBg.style.display = 'block';
    yearLabel.style.display = 'block';
    if (personsElement) {
      personsElement.style.display = 'block';
    }
  });

  cardGroup.addEventListener('mouseleave', () => {
    // Hide all elements except the title
    cardBg.style.display = 'none';
    yearLabel.style.display = 'none';
    if (personsElement) {
      personsElement.style.display = 'none';
    }
  });

  return cardGroup;
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
      let rectWidth = 16; // Default width
      let rectX = x - 8;  // Default x position

      // Check if this event has children and adjust width accordingly
      const rightmostX = parentWidthMap.get(event.key);
      if (rightmostX && rightmostX > event.x) {
        // This event is a parent, expand its rectangle to cover its children
        rectX = x - 8; // Left edge at parent's position
        rectWidth = (rightmostX - x) + 16; // Width to cover up to rightmost child
      } else {
        // Regular event with default width
        rectX = x - 8;
        rectWidth = 16;
      }

      // Generate random color for time range rectangle
      const randomColor = getRandomColor();

      // Time range rectangle
      const rangeRect = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
      rangeRect.setAttribute('x', rectX);
      rangeRect.setAttribute('y', rectY);
      rangeRect.setAttribute('width', rectWidth);
      rangeRect.setAttribute('height', rectHeight);
      rangeRect.setAttribute('fill', randomColor);
      rangeRect.setAttribute('stroke', '#3949ab');
      rangeRect.setAttribute('stroke-width', 1);
      rangeRect.setAttribute('class', 'timeline-range');
      svgElement.appendChild(rangeRect);

      // Event card - position it at the start of the time range
      const cardGroup = createEventCard(event, x, event.startY, true);
      svgElement.appendChild(cardGroup);

      // Add hover effect to the range rectangle to show/hide the card
      rangeRect.addEventListener('mouseenter', () => {
        const cardBg = cardGroup.querySelector('.event-card-bg');
        const yearLabel = cardGroup.querySelector('.event-year');
        const personsElement = cardGroup.querySelector('.event-persons');

        if (cardBg) cardBg.style.display = 'block';
        if (yearLabel) yearLabel.style.display = 'block';
        if (personsElement) personsElement.style.display = 'block';
      });

      rangeRect.addEventListener('mouseleave', () => {
        const cardBg = cardGroup.querySelector('.event-card-bg');
        const yearLabel = cardGroup.querySelector('.event-year');
        const personsElement = cardGroup.querySelector('.event-persons');

        if (cardBg) cardBg.style.display = 'none';
        if (yearLabel) yearLabel.style.display = 'none';
        if (personsElement) personsElement.style.display = 'none';
      });
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
      connector.setAttribute('x2', x - 10);
      connector.setAttribute('y2', event.startY);
      connector.setAttribute('stroke', '#3949ab');
      connector.setAttribute('stroke-width', 1);
      connector.setAttribute('stroke-dasharray', '4,2');
      svgElement.appendChild(connector);

      // Draw event dot
      const marker = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
      marker.setAttribute('cx', x);
      marker.setAttribute('cy', event.startY);
      marker.setAttribute('r', 6);
      marker.setAttribute('class', 'timeline-marker');
      svgElement.appendChild(marker);

      // Event card
      const cardGroup = createEventCard(event, x, event.startY, false);
      svgElement.appendChild(cardGroup);

      // Add hover effect to the marker to show/hide the card
      marker.addEventListener('mouseenter', () => {
        const cardBg = cardGroup.querySelector('.event-card-bg');
        const yearLabel = cardGroup.querySelector('.event-year');
        const personsElement = cardGroup.querySelector('.event-persons');

        if (cardBg) cardBg.style.display = 'block';
        if (yearLabel) yearLabel.style.display = 'block';
        if (personsElement) personsElement.style.display = 'none';
      });

      marker.addEventListener('mouseleave', () => {
        const cardBg = cardGroup.querySelector('.event-card-bg');
        const yearLabel = cardGroup.querySelector('.event-year');
        const personsElement = cardGroup.querySelector('.event-persons');

        if (cardBg) cardBg.style.display = 'none';
        if (yearLabel) yearLabel.style.display = 'none';
        if (personsElement) personsElement.style.display = 'none';
      });
    }
  });
}