# Math Scripts

`math/scripts` is a collection of scripts for syncing, querying, validating, and serving `math.json` together with the Markdown concept notes.

## Overview

| File | Primary Purpose | Description |
| --- | --- | --- |
| `graph.py` | Graph model and `math.json` CRUD | Handles node create/read/update/delete, automatic parent-child relation completion, and JSON I/O |
| `build_graph_from_markdown.py` | Markdown -> JSON | Scans concept Markdown files, builds the graph, and outputs `math.json` |
| `build_markdown_from_graph.py` | JSON -> Markdown | Reconstructs Markdown notes from `math.json` |
| `lookup_concept.py` | Concept lookup | Finds concepts by exact match, substring match, or fuzzy match and returns selected fields |
| `validate_math_json.py` | Data validation | Checks node structure, reference integrity, and bidirectional relation consistency |
| `service.py` | Flask API | Exposes common functions through a unified `POST /function` endpoint |
| `markdown.py` | Markdown parsing helpers | Parses `## Section` blocks and relation-link lines |
| `_math_json_common.py` | Shared utilities | Provides JSON loading, field normalization, fuzzy matching, and other core helpers |
| `sync.html` | Local operations page | Uses browser buttons to call the Flask service for two-way synchronization |

## `graph.py`

### Core Capabilities

| Function/Object | Purpose | Key Notes |
| --- | --- | --- |
| `Node` | A single concept node | Contains `define`, `properties`, `children`, and `parents` |
| `Node.add_child()` | Add a child relation | Automatically syncs the target node's `parents` |
| `Node.add_parent()` | Add a parent relation | Automatically syncs the target node's `children` |
| `Node.remove_child()` | Remove a child relation | Automatically removes the reverse parent relation |
| `Node.remove_parent()` | Remove a parent relation | Automatically removes the reverse child relation |
| `ensure_node_in_graph()` | Ensure a node exists | Automatically creates an empty node if missing |
| `sync_graph_relations()` | Sync bidirectional relations | Can fill in one side from either `children` or `parents` |
| `build_edge_in_graph()` | Create an edge | Uses the shared bidirectional sync logic |
| `build_node_in_graph()` | Create a node from an anchor | Can attach it to the graph as a `kid` or `parent` relation |
| `replace_children()` | Replace all child relations | Removes old relations first, then adds new ones while keeping reverse links consistent |
| `replace_parents()` | Replace all parent relations | Removes old relations first, then adds new ones while keeping reverse links consistent |
| `get_node_from_graph()` | Read a node | Raises an error if the node does not exist |
| `list_nodes_in_graph()` | List node keys | Returns a sorted list of keys |
| `create_node_in_graph()` | Create a new node | Supports initializing definition, properties, and relations |
| `update_node_in_graph()` | Update a node | Supports field updates and relation merge/replace behavior |
| `delete_node_from_graph()` | Delete a node | Automatically clears all connected edges |
| `add_child_in_graph()` | Add one child relation | Relation-level operation |
| `add_parent_in_graph()` | Add one parent relation | Relation-level operation |
| `remove_child_in_graph()` | Remove one child relation | Relation-level operation |
| `remove_parent_in_graph()` | Remove one parent relation | Relation-level operation |
| `serialize_graph()` | Serialize the graph | Automatically completes bidirectional relations before writing |
| `graph_to_json()` | Write the graph to JSON | Saves the graph to the specified path |
| `json_to_graph()` | Load the graph from JSON | Automatically completes bidirectional relations after reading |

### Direct CRUD on `math.json`

| Function | Purpose | Main Parameters |
| --- | --- | --- |
| `list_nodes_in_json()` | List all nodes | `path` |
| `get_node_in_json()` | Read one node | `path`, `key` |
| `create_node_in_json()` | Create a node | `path`, `key`, `define`, `properties`, `children`, `parents` |
| `update_node_in_json()` | Update a node | `path`, `key`, `define`, `properties`, `children`, `parents`, `merge_relations` |
| `delete_node_in_json()` | Delete a node | `path`, `key` |
| `add_child_in_json()` | Add a child relation | `path`, `key`, `child_key`, `label` |
| `add_parent_in_json()` | Add a parent relation | `path`, `key`, `parent_key`, `label` |
| `remove_child_in_json()` | Remove a child relation | `path`, `key`, `child_key` |
| `remove_parent_in_json()` | Remove a parent relation | `path`, `key`, `parent_key` |

### Relation Consistency Rules

| Operation | Automatic Behavior |
| --- | --- |
| Add to `children` | Automatically fills in the target node's `parents` |
| Add to `parents` | Automatically fills in the target node's `children` |
| Delete a node | Automatically removes all related parent-child edges |
| Delete a one-sided relation | Automatically removes the corresponding relation on the other side |
| Read from JSON | Automatically repairs one-sided relations into bidirectional consistency |
| Write back to JSON | Synchronizes relations first, then serializes |

## `build_graph_from_markdown.py`

| Function | Purpose | Description |
| --- | --- | --- |
| `build_graph_json_from_markdown_folder()` | Scan a folder and output JSON | Entry point that accepts `folder_path` and `output_path` |
| `build_graph_from_markdown_folder()` | Build a graph from a folder | Recursively walks through all `.md` files |
| `build_graph_from_markdown_file()` | Parse a single Markdown file | Reads the `Define`, `Properties`, `Include`, and `Parents` sections |
| `build_parser()` / `main()` | CLI entry | Supports running Markdown -> JSON from the command line |

### Input Markdown Convention

| Section | Purpose |
| --- | --- |
| `## Define` | Main definition text for the concept |
| `## Properties` | Properties or supplementary notes |
| `## Include` | List of child relations |
| `## Parents` | List of parent relations |

## `build_markdown_from_graph.py`

| Function | Purpose | Description |
| --- | --- | --- |
| `build_markdown_from_graph_json()` | Rebuild Markdown from JSON | Reads `json_file` and writes output to `output_dir` |
| `build_markdown_from_graph()` | Write Markdown from a graph object | Generates one `.md` file for each node |
| `add_kid_for_graph()` | Add a child node and optionally rebuild Markdown | Compatibility entry point for older calling styles |
| `build_parser()` / `main()` | CLI entry | Supports the `build` and `add-kid` subcommands |

### Generated Markdown Content

| Section | Source |
| --- | --- |
| Title `# ...` | Node key |
| `## Define` | `node.define` |
| `## Properties` | `node.properties` |
| `## Include` | `node.children` |
| `## Parents` | `node.parents` |

## `lookup_concept.py`

| Function | Purpose | Description |
| --- | --- | --- |
| `lookup_concept()` | Query concepts | Supports exact, substring, and fuzzy matching |
| `build_parser()` / `main()` | CLI entry | Supports `--field`, `--path`, and `--max-matches` |

### Lookup Features

| Feature | Description |
| --- | --- |
| Exact match | `term` exactly matches the key or the space-normalized key |
| Substring match | `term` is part of the key |
| Fuzzy match | Scored with `SequenceMatcher` |
| Field selection | Supports `define`, `parents`, `children`, `properties`, or `all` |
| Candidate list | Returns candidates when there is no hit or the result is ambiguous |

## `validate_math_json.py`

| Function | Purpose | Description |
| --- | --- | --- |
| `validate_node_shape()` | Validate one node structure | Checks missing fields, type errors, and unexpected extra fields |
| `format_edge_issue()` | Format edge issue messages | Reports one-sided edges or mismatched labels |
| `validate_math_json()` | Validate the full JSON | Outputs statistics, warnings, errors, and structural issues |
| `build_parser()` / `main()` | CLI entry | Supports `--path`, `--json`, and `--strict` |

### Validation Items

| Type | Description |
| --- | --- |
| Node structure | Whether `define` / `parents` / `children` / `properties` exist and have the correct types |
| Reference integrity | Whether target nodes referenced by parent-child relations actually exist |
| Bidirectional consistency | Whether `A.children[B]` and `B.parents[A]` mirror each other |
| Relation label consistency | Whether labels on both sides of an edge are the same |
| Statistics | Concept count, edge count, property length distribution, and relation label distribution |

## `service.py`

`service.py` starts a Flask service and routes function calls through `POST /function`.

### Request Format

```json
{
  "function": "create_node_in_json",
  "params": {
    "path": "D:/Algo/Notes/math_physics/math/lib/math.json",
    "key": "Example_Node",
    "define": "example"
  }
}
```

### Functions Currently Exposed

| Function Name | Source | Purpose |
| --- | --- | --- |
| `build_graph_json_from_markdown_folder` | `build_graph_from_markdown.py` | Markdown -> JSON |
| `build_markdown_from_graph_json` | `build_markdown_from_graph.py` | JSON -> Markdown |
| `add_kid_for_graph` | `build_markdown_from_graph.py` | Add a child node and optionally rebuild Markdown |
| `list_nodes_in_json` | `graph.py` | List nodes |
| `get_node_in_json` | `graph.py` | Query a node |
| `create_node_in_json` | `graph.py` | Create a node |
| `update_node_in_json` | `graph.py` | Update a node |
| `delete_node_in_json` | `graph.py` | Delete a node |
| `add_child_in_json` | `graph.py` | Add a child relation |
| `add_parent_in_json` | `graph.py` | Add a parent relation |
| `remove_child_in_json` | `graph.py` | Remove a child relation |
| `remove_parent_in_json` | `graph.py` | Remove a parent relation |
| `lookup_concept` | `lookup_concept.py` | Fuzzy concept lookup |
| `validate_math_json` | `validate_math_json.py` | Validate JSON structure and relations |

## `markdown.py`

| Function | Purpose | Description |
| --- | --- | --- |
| `parse_section_in_markdown()` | Extract a specific level-2 heading section | For example, extract the content of `## Define` |
| `parse_kv_links()` | Parse a relation list | Parses lines in the form `- [Node](./Node.md): label` |

## `_math_json_common.py`

| Function/Object | Purpose | Description |
| --- | --- | --- |
| `STANDARD_FIELDS` | Standard field definitions | `define`, `parents`, `children`, `properties` |
| `ConceptMatch` | Match result object | Contains `key`, `match_type`, and `score` |
| `load_concepts()` | Read JSON | Includes file existence checks and JSON format validation |
| `get_standard_field()` | Normalize a field value | Automatically returns a safe default value |
| `render_relation_map()` | Render a relation map | Used for CLI output |
| `select_fields()` | Select returned fields | Supports `all` or a subset |
| `resolve_concept()` | Fuzzy-match a concept | Returns the best hit and a candidate list |

## `sync.html`

| Feature | Description |
| --- | --- |
| Local button actions | Triggers sync operations through UI buttons |
| Flask service integration | Sends requests to `http://127.0.0.1:5000/function` by default |
| Markdown -> JSON | Calls `build_graph_json_from_markdown_folder` |
| JSON -> Markdown | Calls `build_markdown_from_graph_json` |
| Result display | Shows status and logs on the page |

## Common Usage

### 1. Start the service

```powershell
python service.py --host 127.0.0.1 --port 5000
```

### 2. Rebuild JSON from Markdown

```powershell
python build_graph_from_markdown.py D:\Algo\Notes\math_physics\math D:\Algo\Notes\math_physics\math\lib\math.json --json
```

### 3. Rebuild Markdown from JSON

```powershell
python build_markdown_from_graph.py build D:\Algo\Notes\math_physics\math\lib\math.json D:\Algo\Notes\math_physics\math --json
```

### 4. Query a concept

```powershell
python lookup_concept.py manifold --path D:\Algo\Notes\math_physics\math\lib\math.json --field define --field parents
```

### 5. Validate `math.json`

```powershell
python validate_math_json.py --path D:\Algo\Notes\math_physics\math\lib\math.json --json
```
