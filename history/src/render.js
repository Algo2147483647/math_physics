// Clear SVG element
function clearSVG() {
  svgElement.innerHTML = '';
}

// Calculate year range and dimensions
function calculateDimensions() {
  const years = historyData.map(event => parseInt(event.time[0]));
  const minYear = Math.min(...years);
  const maxYear = Math.max(...years);
  const width = 1200;
  const height = Math.max(2000, (maxYear - minYear) * 15);
  svgElement.setAttribute('height', height);
  const margin = { top: 50, right: 50, bottom: 50, left: 150 };
  const innerWidth = width - margin.left - margin.right;
  const innerHeight = height - margin.top - margin.bottom;

  return { minYear, maxYear, width, height, margin, innerWidth, innerHeight };
}

// Create year-to-position mapping function
function createYearScale(minYear, maxYear, margin, innerHeight) {
  return (year) => {
    return margin.top + ((year - minYear) / (maxYear - minYear)) * innerHeight;
  };
}

// Draw vertical timeline
function drawVerticalTimeline(height, margin) {
  const timelineLine = document.createElementNS('http://www.w3.org/2000/svg', 'line');
  timelineLine.setAttribute('x1', margin.left);
  timelineLine.setAttribute('y1', margin.top);
  timelineLine.setAttribute('x2', margin.left);
  timelineLine.setAttribute('y2', height - margin.bottom);
  timelineLine.setAttribute('class', 'timeline-line');
  svgElement.appendChild(timelineLine);
}

// Add year ticks to timeline
function addYearTicks(minYear, maxYear, yearScale, margin, height) {
  const yearInterval = 10;
  let firstYear = Math.ceil(minYear / 10) * 10;
  if (firstYear > maxYear) {
    firstYear = Math.floor(minYear / 10) * 10;
  }
  
  for (let year = firstYear; year <= maxYear; year += yearInterval) {
    const y = yearScale(year);

    if (y >= margin.top && y <= height - margin.bottom) {
      // 刻度线
      const tickLine = document.createElementNS('http://www.w3.org/2000/svg', 'line');
      tickLine.setAttribute('x1', margin.left - 5);
      tickLine.setAttribute('y1', y);
      tickLine.setAttribute('x2', margin.left + 5);
      tickLine.setAttribute('y2', y);
      tickLine.setAttribute('stroke', '#7986cb');
      tickLine.setAttribute('stroke-width', 1);
      svgElement.appendChild(tickLine);

      // Year label - use plus/minus signs instead of BC/AD
      const yearLabel = document.createElementNS('http://www.w3.org/2000/svg', 'text');
      yearLabel.setAttribute('x', margin.left - 10);
      yearLabel.setAttribute('y', y + 4);
      yearLabel.setAttribute('text-anchor', 'end');
      yearLabel.setAttribute('font-size', '10');
      yearLabel.setAttribute('fill', '#555');

      let yearDisplay = year < 0 ? `-${Math.abs(year)}` : `${year}`;
      yearLabel.textContent = yearDisplay;
      svgElement.appendChild(yearLabel);
    }
  }
}

// Process events to determine if they are single points or time ranges
function processEvents(yearScale) {
  return historyData.map((event, index) => {
    const isTimeRange = event.time.length > 1;
    const startTime = parseInt(event.time[0]);
    const endTime = isTimeRange ? parseInt(event.time[1]) : startTime;
    const startY = yearScale(startTime);
    const endY = yearScale(endTime);

    return {
      ...event,
      isTimeRange,
      startTime,
      endTime,
      startY,
      endY
    };
  });
}

// Separate time ranges and single points
function separateEvents(timelineData) {
  const timeRanges = timelineData.filter(event => event.isTimeRange);
  const singlePoints = timelineData.filter(event => !event.isTimeRange);
  return { timeRanges, singlePoints };
}

// Create event card SVG group
function createEventCard(event, x, y, isTimeRange = false) {
  const cardGroup = document.createElementNS('http://www.w3.org/2000/svg', 'g');
  cardGroup.setAttribute('class', 'event-card');
  cardGroup.addEventListener('click', () => showEventDetails(event));

  // Card background
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
  cardGroup.appendChild(cardBg);

  // Event title
  const title = document.createElementNS('http://www.w3.org/2000/svg', 'text');
  title.setAttribute('x', x + 120);
  title.setAttribute('y', y - 15);
  title.setAttribute('text-anchor', 'middle');
  title.setAttribute('class', 'event-title');
  title.textContent = truncateText(event.key || 'N/A', 25);
  cardGroup.appendChild(title);

  // Year label
  const yearLabel = document.createElementNS('http://www.w3.org/2000/svg', 'text');
  yearLabel.setAttribute('x', x + 120);
  yearLabel.setAttribute('y', y + 5);
  yearLabel.setAttribute('text-anchor', 'middle');
  yearLabel.setAttribute('class', 'event-year');

  let yearDisplay;
  if (isTimeRange) {
    yearDisplay = `${event.startTime < 0 ? `-${Math.abs(event.startTime)}` : `+${event.startTime}`} - ${event.endTime < 0 ? `-${Math.abs(event.endTime)}` : `+${event.endTime}`}`;
  } else {
    yearDisplay = event.startTime < 0 ? `-${Math.abs(event.startTime)}` : `+${event.startTime}`;
  }
  yearLabel.textContent = yearDisplay;
  cardGroup.appendChild(yearLabel);

  // Person information
  if (event.data.persons) {
    const persons = document.createElementNS('http://www.w3.org/2000/svg', 'text');
    persons.setAttribute('x', x + 120);
    persons.setAttribute('y', y + 20);
    persons.setAttribute('text-anchor', 'middle');
    persons.setAttribute('class', 'event-persons');
    persons.textContent = truncateText(Array.isArray(event.data.persons) ? event.data.persons.join(', ') : event.data.persons, 25);
    cardGroup.appendChild(persons);
  }

  return cardGroup;
}

// Draw time ranges
function drawTimeRanges(timeRanges, margin, height, yearScale) {
  timeRanges.forEach((event) => {
    const x = event.x;

    if (event.startY >= margin.top && event.startY <= height - margin.bottom) {
      // For time ranges, draw a narrow rectangle
      const rectHeight = Math.abs(event.endY - event.startY);
      const rectY = Math.min(event.startY, event.endY);

      // Generate random color for time range rectangle
      const randomColor = getRandomColor();

      // Time range rectangle
      const rangeRect = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
      rangeRect.setAttribute('x', x - 8);
      rangeRect.setAttribute('y', rectY);
      rangeRect.setAttribute('width', 16);
      rangeRect.setAttribute('height', rectHeight);
      rangeRect.setAttribute('fill', randomColor);
      rangeRect.setAttribute('stroke', '#3949ab');
      rangeRect.setAttribute('stroke-width', 1);
      rangeRect.setAttribute('class', 'timeline-range');
      svgElement.appendChild(rangeRect);

      // Event card - position it at the start of the time range
      const cardGroup = createEventCard(event, x, event.startY, true);
      svgElement.appendChild(cardGroup);
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
    }
  });
}

// Render SVG timeline
function renderTimeline() {
  // Clear SVG
  clearSVG();

  // Calculate dimensions
  const { minYear, maxYear, width, height, margin, innerWidth, innerHeight } = calculateDimensions();

  // Calculate year-to-position mapping
  const yearScale = createYearScale(minYear, maxYear, margin, innerHeight);

  // Draw vertical timeline
  drawVerticalTimeline(height, margin);

  // Add year ticks
  addYearTicks(minYear, maxYear, yearScale, margin, height);

  // Process events
  timelineData = processEvents(yearScale);

  // Separate time ranges and single points
  const { timeRanges, singlePoints } = separateEvents(timelineData);

  // Calculate horizontal positions for time ranges and single points to avoid conflicts
  calculateHorizontalPositions(timeRanges, singlePoints, margin);

  // Draw time ranges first
  drawTimeRanges(timeRanges, margin, height, yearScale);

  // Draw single points separately
  drawSinglePoints(singlePoints, margin, height);
}