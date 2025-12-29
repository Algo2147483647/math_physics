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
  cardBg.setAttribute('x', x - 100);
  cardBg.setAttribute('y', y - 40);
  cardBg.setAttribute('width', 200);
  cardBg.setAttribute('height', 70);
  cardBg.setAttribute('rx', 12);
  cardBg.setAttribute('ry', 12);
  cardBg.setAttribute('fill', 'white');
  cardBg.setAttribute('stroke', 'transparent');
  cardBg.setAttribute('stroke-width', 1);
  cardBg.setAttribute('class', 'event-card-bg');
  cardBg.style.display = 'none'; // Initially hidden
  cardGroup.appendChild(cardBg);

  // Event title (always visible)
  const title = document.createElementNS('http://www.w3.org/2000/svg', 'text');
  title.setAttribute('x', x);
  title.setAttribute('y', y - 20);
  title.setAttribute('text-anchor', 'middle');
  title.setAttribute('class', 'event-title');
  title.textContent = truncateText(event.key || 'N/A', 25);
  cardGroup.appendChild(title);

  // Year label (initially hidden)
  const yearLabel = document.createElementNS('http://www.w3.org/2000/svg', 'text');
  yearLabel.setAttribute('x', x);
  yearLabel.setAttribute('y', y);
  yearLabel.setAttribute('text-anchor', 'middle');
  yearLabel.setAttribute('class', 'event-year');
  yearLabel.style.display = 'none'; // Initially hidden

  let yearDisplay;
  if (isTimeRange) {
    yearDisplay = event.startTime < 0 ? '-' + Math.abs(event.startTime) + ' ~ ' + (event.endTime < 0 ? '-' + Math.abs(event.endTime) : event.endTime) : event.startTime + ' ~ ' + (event.endTime < 0 ? '-' + Math.abs(event.endTime) : event.endTime);
  } else {
    yearDisplay = event.startTime < 0 ? '-' + Math.abs(event.startTime) : event.startTime;
  }
  yearLabel.textContent = yearDisplay;
  cardGroup.appendChild(yearLabel);

  // Person information (initially hidden)
  let personsElement = null;
  if (event.data.persons) {
    personsElement = document.createElementNS('http://www.w3.org/2000/svg', 'text');
    personsElement.setAttribute('x', x);
    personsElement.setAttribute('y', y + 15);
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

      // Generate softer color for time range rectangle
      const softColor = getSoftColor();

      // Time range rectangle
      const rangeRect = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
      rangeRect.setAttribute('x', rectX);
      rangeRect.setAttribute('y', rectY);
      rangeRect.setAttribute('width', rectWidth);
      rangeRect.setAttribute('height', rectHeight);
      rangeRect.setAttribute('fill', softColor);
      rangeRect.setAttribute('stroke', 'transparent');
      rangeRect.setAttribute('stroke-width', 1);
      rangeRect.setAttribute('rx', 8);
      rangeRect.setAttribute('ry', 8);
      rangeRect.setAttribute('class', 'timeline-range');
      svgElement.appendChild(rangeRect);

      // Add gradient overlay to time range for better visual effect
      const gradientId = `gradient-${event.key.replace(/[^a-zA-Z0-9]/g, '')}`;
      const defs = svgElement.querySelector('defs') || document.createElementNS('http://www.w3.org/2000/svg', 'defs');
      if (!svgElement.querySelector('defs')) {
        svgElement.appendChild(defs);
      }
      
      const gradient = document.createElementNS('http://www.w3.org/2000/svg', 'linearGradient');
      gradient.setAttribute('id', gradientId);
      gradient.setAttribute('x1', '0%');
      gradient.setAttribute('y1', '0%');
      gradient.setAttribute('x2', '100%');
      gradient.setAttribute('y2', '0%');
      
      const stop1 = document.createElementNS('http://www.w3.org/2000/svg', 'stop');
      stop1.setAttribute('offset', '0%');
      stop1.setAttribute('stop-color', softColor);
      stop1.setAttribute('stop-opacity', '0.8');
      
      const stop2 = document.createElementNS('http://www.w3.org/2000/svg', 'stop');
      stop2.setAttribute('offset', '100%');
      stop2.setAttribute('stop-color', softColor);
      stop2.setAttribute('stop-opacity', '0.4');
      
      gradient.appendChild(stop1);
      gradient.appendChild(stop2);
      defs.appendChild(gradient);
      
      // Event card - position it at the start of the time range
      const cardGroup = createEventCard(event, x, event.startY, true);
      svgElement.appendChild(cardGroup);

      // Add hover effect to the range rectangle to show/hide the card
      rangeRect.addEventListener('mouseenter', () => {
        const cardBg = cardGroup.querySelector('.event-card-bg');
        const yearLabel = cardGroup.querySelector('.event-year');
        const personsElement = cardGroup.querySelector('.event-persons');
        const paperElement = cardGroup.querySelector('.event-paper');

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
      connector.setAttribute('x2', x - 15);
      connector.setAttribute('y2', event.startY);
      connector.setAttribute('stroke', '#c5d0e6');
      connector.setAttribute('stroke-width', 2);
      connector.setAttribute('stroke-dasharray', '6,4');
      svgElement.appendChild(connector);

      // Draw event marker background circle for better visual
      const markerBg = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
      markerBg.setAttribute('cx', x);
      markerBg.setAttribute('cy', event.startY);
      markerBg.setAttribute('r', 12);
      markerBg.setAttribute('class', 'timeline-marker-bg');
      svgElement.appendChild(markerBg);

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
        const paperElement = cardGroup.querySelector('.event-paper');

        if (cardBg) cardBg.style.display = 'block';
        if (yearLabel) yearLabel.style.display = 'block';
        if (personsElement) personsElement.style.display = 'block';
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