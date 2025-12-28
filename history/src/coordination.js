// Calculate horizontal positions for time ranges and single points to avoid conflicts using DFS
function calculateHorizontalPositions(events, margin) {
  const minSpacing = 16; // Minimum spacing between events

  // Create a map of all events for easy lookup
  const allEventsMap = new Map();
  events.forEach(event => allEventsMap.set(event.key, event));

  console.log(allEventsMap)
  
  const roots = []; // Events without parents, Populate children map and find root nodes
  events.forEach(event => {
    if (!event.parents || event.parents.length == 0 || event.parents[0] === '') {
      roots.push(event);
    }
  });

  // Sort root nodes by vertical position
  roots.sort((a, b) => a.startY - b.startY);
  
  // Process root nodes using DFS and store all positioned events
  const positionedEvents = [];
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

  console.log(kids)

  kids.sort((a, b) => {
    console.log(a, allEventsMap[a]);
    console.log(b, allEventsMap[b]);
    return allEventsMap[a].startTime - allEventsMap[b].startTime;
  });
  
  // Process all children of the current event
  kids.forEach(kid => {
    processEventDFS(allEventsMap[kid], event.x + minSpacing, minSpacing, allEventsMap, positionedEvents);
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
  // Check if the y-ranges overlap
  const yOverlap = !(currentEvent.endTime < otherEvent.startTime || currentEvent.startTime > otherEvent.endTime);

  // Check if x-positions are too close
  const xTooClose = Math.abs(currentX - otherEvent.x) < minSpacing;

  // Conflict occurs if both y-ranges overlap and x-positions are too close
  return yOverlap && xTooClose;
}