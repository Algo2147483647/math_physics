
// Calculate horizontal positions for time ranges and single points to avoid conflicts
function calculateHorizontalPositions(timeRanges, singlePoints, margin) {
  // Sort events by vertical position to process them in order
  timeRanges.sort((a, b) => a.startY - b.startY);
  singlePoints.sort((a, b) => a.startY - b.startY);

  const minSpacing = 16; // Minimum spacing between events

  // Process time ranges first
  for (let i = 0; i < timeRanges.length; i++) {
    const currentEvent = timeRanges[i];
    // Find the minimal x position that doesn't conflict with already positioned events
    currentEvent.x = findNonConflictingXPositionForEvent(currentEvent, timeRanges.slice(0, i), singlePoints, margin.left + 40, minSpacing);
  }

  // Process single points
  for (let i = 0; i < singlePoints.length; i++) {
    const currentEvent = singlePoints[i];
    // Find the minimal x position that doesn't conflict with all positioned events
    currentEvent.x = findNonConflictingXPositionForEvent(currentEvent, timeRanges, singlePoints.slice(0, i), margin.left + 40, minSpacing);
  }
}

// Helper function to find a non-conflicting x position for an event
function findNonConflictingXPositionForEvent(currentEvent, positionedTimeRanges, positionedSinglePoints, initialX, minSpacing) {
  // Start with initial x position
  let x = initialX;

  // Create a list of all positioned events to check against
  const allPositionedEvents = [...positionedTimeRanges, ...positionedSinglePoints];

  // Check against all existing positioned events to avoid conflicts
  let hasConflict = true;
  while (hasConflict) {
    hasConflict = false;

    for (const positionedEvent of allPositionedEvents) {
      if (doesConflict(currentEvent, positionedEvent, x, minSpacing)) {
        // Move x position past the conflicting event
        x = positionedEvent.x + minSpacing;
        hasConflict = true;
        break;
      }
    }
  }

  return x;
}

// Helper function to determine if two events conflict at a given x position
function doesConflict(currentEvent, otherEvent, currentX, minSpacing) {
  // For time ranges, we need to consider the full height of the rectangle
  let currentTop, currentBottom;

  if (currentEvent.isTimeRange) {
    currentTop = Math.min(currentEvent.startY, currentEvent.endY);
    currentBottom = Math.max(currentEvent.startY, currentEvent.endY);
  } else {
    // For single points, consider the point position with some tolerance
    currentTop = currentEvent.startY;
    currentBottom = currentEvent.startY;
  }

  let otherTop, otherBottom;

  if (otherEvent.isTimeRange) {
    otherTop = Math.min(otherEvent.startY, otherEvent.endY);
    otherBottom = Math.max(otherEvent.startY, otherEvent.endY);
  } else {
    // For single points, consider the point position with some tolerance
    otherTop = otherEvent.startY;
    otherBottom = otherEvent.startY;
  }

  // Check if the y-ranges overlap
  const yOverlap = !(currentBottom < otherTop || currentTop > otherBottom);

  // Check if x-positions are too close
  const xTooClose = Math.abs(currentX - otherEvent.x) < minSpacing;

  // Conflict occurs if both y-ranges overlap and x-positions are too close
  return yOverlap && xTooClose;
}
