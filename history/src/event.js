// 对所有事件 timelineData 的父子关系进行对齐，缺少的话补充上去，即保证每个节点的parent和kids都是对的，不缺少的
function alignParentChildRelationships(events) {
  // 首先，清空所有事件的 kids 数组
  events.forEach(event => {
    if (!event.kids) {
      event.kids = [];
    }
  });

  // 遍历所有事件，建立正确的父子关系
  events.forEach(event => {
    // 确保 parents 数组存在
    if (!event.parents || !Array.isArray(event.parents)) {
      event.parents = [];
    }

    // 遍历当前事件的每个 parent
    event.parents.forEach(parentKey => {
      if (parentKey && parentKey.trim() !== "") {
        // 在 events 中查找该 parent 事件
        const parentEvent = events.find(e => e.key === parentKey);

        if (parentEvent) {
          // 确保 parent 事件的 kids 数组存在
          if (!parentEvent.kids || !Array.isArray(parentEvent.kids)) {
            parentEvent.kids = [];
          }

          // 检查是否已经存在于 parent 的 kids 数组中
          if (!parentEvent.kids.includes(event.key)) {
            parentEvent.kids.push(event.key);
          }
        }
      }
    });

    // 同样，遍历当前事件的每个 kid
    if (event.kids && Array.isArray(event.kids)) {
      event.kids.forEach(kidKey => {
        if (kidKey && kidKey.trim() !== "") {
          // 在 events 中查找该 kid 事件
          const kidEvent = events.find(e => e.key === kidKey);

          if (kidEvent) {
            // 确保 kid 事件的 parents 数组存在
            if (!kidEvent.parents || !Array.isArray(kidEvent.parents)) {
              kidEvent.parents = [];
            }

            // 检查是否已经存在于 kid 的 parents 数组中
            if (!kidEvent.parents.includes(event.key)) {
              kidEvent.parents.push(event.key);
            }
          }
        }
      });
    }
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


