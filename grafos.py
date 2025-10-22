from queue import PriorityQueue


grafo = {
    'Ylane': {'Strento':99, 'Oriaron':117, 'Goding':88 },
    'Strento': {'Ylane':99, 'Zrusall':121, 'Oriaron':221},
    'Zrusall': {'Strento':121, 'Goxmont':112, 'Adaset': 15},
    'Goxmont': {'Zrusall':112, 'Adaset':103, 'Niaphia': 212},
    'Niaphia': {'Goxmont':212, 'Ertonwell': 56, 'Lagos':300},
    'Lagos': {'Niaphia': 300, 'Duron':119},
    'Duron': {'Ertonwell':121, 'Blebus': 160, 'Lagos': 119},
    'Blebus': {'Duron': 160, 'Oriaron':291, 'Ontdale':165, 'Togend': 121},
    'Togend': {'Blebus':121, 'Ontdale':210},
    'Ontdale': {'Togend': 210, 'Blebus':165, 'Oriaron': 219, 'Goding': 98},
    'Goding': {'Ontdale':98, 'Ylane': 88}, 
    'Adaset': {'Zrusall': 15, 'Goxmont': 103, 'Ertonwell': 130}, 
    'Ertonwell': {'Adaset':130, 'Niaphia': 56, 'Duron': 121}, 
    'Oriaron': {'Blebus':291, 'Ontdale':219, 'Ylane':117, 'Strento': 221}
}

