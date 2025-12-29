// Calculate horizontal positions for time ranges and single points to avoid conflicts using DFS
function calculateHorizontalPositions(events) {
  // Create a map of all events for easy lookup
  const allEventsMap = new Map();
  events.forEach(event => allEventsMap.set(event.key, event));

  const virtualRoot = {
    key: 'virtualRoot',
    parents: [],
    kids: getRoots(events).map(root => root.key),
    startTime: -Infinity,
    endTime: Infinity,
  };

  processEventDFS(virtualRoot, allEventsMap, []);
}

// Process an event and its children using DFS
function processEventDFS(event, allEventsMap, positionedEvents) {
  // 1. Get kids of the current event
  const kids = event.kids || [];
  if (!kids || kids.length == 0) {
    event.width = 1;
    findNonConflictingXPositionForEvent(event, positionedEvents);
    positionedEvents.push(event);
    return;
  }

  kids.sort((a, b) => allEventsMap.get(a).startTime - allEventsMap.get(b).startTime);
  
  // 2. Process all kids of the current event
  const positionedEventsTmp = [];
  kids.forEach(kid => {
    const kidEvent = allEventsMap.get(kid);
    if (kidEvent) {
      processEventDFS(kidEvent, allEventsMap, positionedEventsTmp);
    }
  });

  // 3. get width
  let width = 0
  for (const item of positionedEventsTmp) {
    if (item.x + item.width - 1 > width) {
      width = item.x + item.width - 1;
    }
  }

  // 4. findNonConflictingXPositionForEvent
  event.width = width + 2;
  findNonConflictingXPositionForEvent(event, positionedEvents);
  for (const item of positionedEventsTmp) {
    item.x = item.x + event.x + 1;
  }

  // 5. update positionedEvents
  positionedEvents.push(event);
  positionedEvents.push(...positionedEventsTmp);
  return;
}


// Helper function to find a non-conflicting x position for an event
function findNonConflictingXPositionForEvent(event, positionedEvents) {
  // Start with initial x position
  event.x = 0;

  // Check against all existing positioned events to avoid conflicts
  let hasConflict;
  do {
    hasConflict = false;

    for (const item of positionedEvents) {
      if (isConflict(event, item)) {
        event.x = item.x + item.width; // Move x position past the conflicting event
        hasConflict = true;
        break;
      }
    }
  } while (hasConflict);
}

// Helper function to determine if two events conflict
function isConflict(a, b) {
  const yOverlap = a.endTime >= b.startTime && a.startTime <= b.endTime;
  const xOverlap = a.x + a.width - 1 >= b.x && a.x <= b.x + b.width - 1;
  return yOverlap && xOverlap;
}