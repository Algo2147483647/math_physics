// Calculate horizontal positions for time ranges and single points to avoid conflicts using DFS
function calculateHorizontalPositions(timeRanges, singlePoints, margin) {
  const minSpacing = 16; // Minimum spacing between events
  
  // Create a map of all events for easy lookup
  const allEventsMap = new Map();
  [...timeRanges, ...singlePoints].forEach(event => allEventsMap.set(event.key, event));
  
  // Build parent-child relationships
  const childrenMap = new Map(); // Maps parent key to array of children
  const roots = []; // Events without parents
  
  // Initialize children map
  [...timeRanges, ...singlePoints].forEach(event => {
    childrenMap.set(event.key, { timeRanges: [], singlePoints: [] });
  });
  
  // Populate children map and find root nodes
  timeRanges.forEach(event => {
    if (event.parents && event.parents.length > 0) {
      const parentKey = event.parents[0]; // Assuming single parent for now
      if (parentKey && parentKey.trim() !== "" && allEventsMap.has(parentKey)) {
        const parentChildren = childrenMap.get(parentKey);
        if (parentChildren) {
          parentChildren.timeRanges.push(event);
        }
      } else {
        roots.push(event); // No parent, so it's a root
      }
    } else {
      roots.push(event); // No parent, so it's a root
    }
  });
  
  singlePoints.forEach(event => {
    if (event.parents && event.parents.length > 0) {
      const parentKey = event.parents[0]; // Assuming single parent for now
      if (parentKey && parentKey.trim() !== "" && allEventsMap.has(parentKey)) {
        const parentChildren = childrenMap.get(parentKey);
        if (parentChildren) {
          parentChildren.singlePoints.push(event);
        }
      } else {
        roots.push(event); // No parent, so it's a root
      }
    } else {
      roots.push(event); // No parent, so it's a root
    }
  });
  
  // Sort root nodes by vertical position
  roots.sort((a, b) => a.startY - b.startY);
  
  // Process root nodes using DFS and store all positioned events
  const positionedEvents = [];
  
  roots.forEach(root => {
    processEventDFS(root, margin.left + 40, minSpacing, allEventsMap, childrenMap, positionedEvents);
  });
}

// Process an event and its children using DFS
function processEventDFS(event, baseX, minSpacing, allEventsMap, childrenMap, positionedEvents) {
  // Find a non-conflicting x position for the current event
  event.x = findNonConflictingXPositionForEvent(event, 
    positionedEvents.filter(e => e.isTimeRange), 
    positionedEvents.filter(e => !e.isTimeRange), 
    baseX, minSpacing);
  
  // Add the current event to positioned events
  positionedEvents.push(event);
  
  // Get children of the current event
  const children = childrenMap.get(event.key);
  if (!children) return; // No children to process
  
  // Sort children by vertical position to process them in order
  const allChildren = [...children.timeRanges, ...children.singlePoints];
  allChildren.sort((a, b) => a.startY - b.startY);
  
  // Process all children of the current event
  allChildren.forEach(child => {
    // Child should be positioned to the right of parent, with some offset
    const childBaseX = event.x + minSpacing; // Leave space for parent
    
    // Process this child and its descendants recursively
    processEventDFS(child, childBaseX, minSpacing, allEventsMap, childrenMap, positionedEvents);
  });
}

// Helper function to find a parent event by key
function findParentEvent(parentKey, allEvents) {
  return allEvents.find(event => event.key === parentKey);
}

// Helper function to find a non-conflicting x position for an event
function findNonConflictingXPositionForEvent(currentEvent, positionedTimeRanges, positionedSinglePoints, initialX, minSpacing) {
  // Start with initial x position
  let x = initialX;

  // Create a list of all positioned events to check against
  const allPositionedEvents = [...positionedTimeRanges, ...positionedSinglePoints];

  // Check against all existing positioned events to avoid conflicts
  let hasConflict;
  do {
    hasConflict = false;

    for (const positionedEvent of allPositionedEvents) {
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