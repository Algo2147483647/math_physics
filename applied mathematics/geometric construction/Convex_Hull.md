# Convex Hull

[TOC]

## Problem

Find the [convex hull](../../math/Convex_Hull.md) from a set of points.

## Resolution

A **convex hull** of a set of points is the smallest convex polygon that can enclose all the points. 

![img](./assets/GrahamScanDemo.gif)

### Process

#### Find Minimum Point

It finds the bottom-most (or left-most if there are ties) point among the given points. This point is guaranteed to be part of the convex hull.

#### Sort Points by Polar Angle

The points are sorted based on their polar angle with respect to the minimum point. This makes sure that when traversing these points in the sorted order, one forms a counterclockwise loop.

#### Construct the Convex Hull

The sorted points are traversed to construct the convex hull:
- It initializes the convex hull with the first two points.
- For each subsequent point, it checks if adding this point to the convex hull would still result in a convex shape.
- This is done by using the cross-product to check the orientation of the triplet formed by the last two points in the hull and the current point.
- If the shape is not convex, the second-to-last point is removed from the hull.