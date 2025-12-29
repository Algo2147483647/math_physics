function getRoots(events) {
  const roots = [];
  events.forEach(event => {
    if (!event.parents || event.parents.length == 0 || event.parents[0] === '') {
      roots.push(event);
    }
  });

  // Sort root nodes by vertical position
  roots.sort((a, b) => a.startTime - b.startTime);
  return roots;
}


// 对所有事件 timelineData 的父子关系进行对齐，缺少的话补充上去，即保证每个节点的parent和kids都是对的，不缺少的
function alignParentChildRelationships(events) {
  events.forEach(event => {
    if (!event.parents || !Array.isArray(event.parents)) {
      event.parents = [];
    }

    if (!event.kids || !Array.isArray(event.kids)) {
      event.kids = [];
    }


    parents = []
    event.parents.forEach(parentKey => {
      if (parentKey && parentKey.trim() !== "") {
        parents.push(parentKey);

        const parentEvent = events.find(e => e.key === parentKey);

        if (parentEvent) {
          if (!parentEvent.kids || !Array.isArray(parentEvent.kids)) {
            parentEvent.kids = [];
          }

          if (!parentEvent.kids.includes(event.key)) {
            parentEvent.kids.push(event.key);
          }
        }
      }
    })
    event.parents = parents;


    kids = []
    event.kids.forEach(kidKey => {
      if (kidKey && kidKey.trim() !== "") {
        kids.push(kidKey);

        const kidEvent = events.find(e => e.key === kidKey);

        if (kidEvent) {
          if (!kidEvent.parents || !Array.isArray(kidEvent.parents)) {
            kidEvent.parents = [];
          }

          if (!kidEvent.parents.includes(event.key)) {
            kidEvent.parents.push(event.key);
          }
        }
      }
    })
    event.kids = kids
  });
}

// Helper function to find a parent event by key
function findParentEvent(parentKey, allEvents) {
  return allEvents.find(event => event.key === parentKey);
}


// Calculate year range and dimensions
function calculateDimensions() {
  const years = historyData.map(event => parseInt(event.time[0]));
  const minYear = Math.min(...years);
  const maxYear = Math.max(...years);
  const width = 1200;
  const height = Math.max(2000, (maxYear - minYear) * 20);
  svgElement.setAttribute('height', height);
  const margin = { top: 50, right: 50, bottom: 50, left: 150 };
  const innerWidth = width - margin.left - margin.right;
  const innerHeight = height - margin.top - margin.bottom;

  return { minYear, maxYear, width, height, margin, innerWidth, innerHeight };
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


