// Calculate horizontal positions for time ranges and single points to avoid conflicts using DFS
function calculateHorizontalPositions(events, margin) {
  const minSpacing = 16; // Minimum spacing between events

  // Create a map of all events for easy lookup
  const allEventsMap = new Map();
  events.forEach(event => allEventsMap.set(event.key, event));

  // Process root nodes using DFS and store all positioned events
  const positionedEvents = [];
  const roots = getRoots(events);
  roots.forEach(root => {
    processEventDFS(root, margin.left + 40, minSpacing, allEventsMap, positionedEvents);
  });
}

// Process an event and its children using DFS
function processEventDFS(event, baseX, minSpacing, allEventsMap, positionedEvents) {
  // Find a non-conflicting x position for the current event
  event.x = findNonConflictingXPositionForEvent(event, positionedEvents, baseX, minSpacing);

  // Add the current event to positioned events
  positionedEvents.push(event);
  
  // Get children of the current event
  const kids = event.kids || [];
  if (!kids || kids.length == 0) return; // No children to process

  kids.sort((a, b) => allEventsMap.get(a).startTime - allEventsMap.get(b).startTime);
  
  // Process all children of the current event
  kids.forEach(kid => {
    const kidEvent = allEventsMap.get(kid);
    if (kidEvent) {
      processEventDFS(kidEvent, event.x + minSpacing, minSpacing, allEventsMap, positionedEvents);
    }
  });
}


// Helper function to find a non-conflicting x position for an event
function findNonConflictingXPositionForEvent(currentEvent, positionedEvents, initialX, minSpacing) {
  // Start with initial x position
  let x = initialX;

  // Check against all existing positioned events to avoid conflicts
  let hasConflict;
  do {
    hasConflict = false;

    for (const positionedEvent of positionedEvents) {
      if (doesConflict(currentEvent, positionedEvent, x, minSpacing)) {
        // Move x position past the conflicting event
        x = positionedEvent.x + minSpacing;
        hasConflict = true;
        break;
      }
    }
  } while (hasConflict);

  return x;
}

// Helper function to determine if two events conflict at a given x position
function doesConflict(currentEvent, otherEvent, currentX, minSpacing) {
  // Handle case where otherEvent might be undefined
  if (!otherEvent) {
    return false; // No conflict if other event doesn't exist
  }
  
  // Check if the y-ranges overlap
  const yOverlap = currentEvent.endTime >= otherEvent.startTime && currentEvent.startTime <= otherEvent.endTime;

  // Check if x-positions are too close
  const xTooClose = Math.abs(currentX - otherEvent.x) < minSpacing;

  // Conflict occurs if both y-ranges overlap and x-positions are too close
  return yOverlap && xTooClose;
}