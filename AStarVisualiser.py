import heapq

import matplotlib.pyplot as plt
import networkx as nx
from networkx import Graph


# TODO: Improve current step visualisation
class AStarVisualiser:

    def visualise_a_star(self,
                         graph: dict,
                         start_node: str,
                         goal_node: str,
                         heuristic,
                         animation_delay=2):
        """
        Реализация на A* алгоритъм с визуализация на стъпките за намиране на най-кратък път.

        :param animation_delay: Задържане на рисуването на графа (сек.)
        :param graph: Списък на съседство, представящ графа (dictionary).
        :param start_node: Началният възел.
        :param goal_node: Крайният възел.
        :param heuristic: Евристична функция за оценка на разстоянието до целта.
        :return: Най-краткият път и общата му тежест.
        """

        # g_score = дължина на път до възела
        # heuristic = потенциална отдалеченост на възела от целта
        # f_score = g_score + heuristic

        open_set = [(0 + heuristic[start_node], start_node, 0, [])]  # (f_score, node, g_score, path)
        closed_set = set()

        # Подготовка за визуализация
        G, layout = self.__initialise_nx_graph(graph)

        while open_set:
            _, current_node, g_score, path = heapq.heappop(open_set)
            print(f'Най-добър следващ възел: {current_node}')

            if current_node == goal_node:
                path = path + [current_node]
                self.__visualise_result(G, layout, path, start_node, current_node, goal_node)
                return path, g_score

            if current_node in closed_set:
                continue

            closed_set.add(current_node)

            # Визуализация на текущото състояние
            self.__visualise_step(G, layout, path, start_node, current_node, goal_node, animation_delay=animation_delay)

            # Разглеждаме съседите на текущия възел
            for neighbor, weight in graph[current_node]:
                if neighbor not in closed_set:
                    tentative_g_score = g_score + weight
                    heapq.heappush(
                        open_set,
                        (tentative_g_score + heuristic[neighbor], neighbor, tentative_g_score, path + [current_node])
                    )
                    print(
                        f"Текущ възел: {current_node}\n"
                        f"  Съсед: {neighbor}\n"
                        f"  Тегло: {weight}\n"
                        f"  Временен g_score: {tentative_g_score}\n"
                        f"  Текущ път: {path}\n"
                        f"  Отворено списък:\n     " + "\n    ".join([f"{item}" for item in open_set]) + "\n"
                    )

        return None, float('inf')

    @staticmethod
    def __visualise_step(graph: Graph,
                         layout: dict,
                         path,
                         start_node,
                         current_node,
                         target_node,
                         node_highlight_color='yellow',
                         animation_delay=2):
        plt.clf()
        nx.draw(graph, layout, with_labels=True, node_color='lightblue', edge_color='gray', node_size=700,
                font_size=15)
        nx.draw_networkx_edge_labels(graph, layout,
                                     edge_labels={(u, v): d['weight'] for u, v, d in graph.edges(data=True)})
        nx.draw_networkx_nodes(graph, layout, nodelist=path + [current_node], node_color=node_highlight_color)
        nx.draw_networkx_nodes(graph, layout, nodelist=[start_node], node_color='white')
        nx.draw_networkx_nodes(graph, layout, nodelist=[target_node], node_color='red')
        nx.draw_networkx_edges(graph, layout, edgelist=[(path[i], path[i + 1]) for i in range(len(path) - 1)],
                               edge_color='red', width=2.5)
        if animation_delay > 0:
            plt.pause(animation_delay)

        plt.show()

    @classmethod
    def __visualise_result(cls,
                           graph: Graph,
                           layout: dict,
                           path,
                           start_node,
                           current_node,
                           target_node):
        cls.__visualise_step(graph, layout, path, start_node, current_node, target_node, node_highlight_color='green', animation_delay=0)

    @staticmethod
    def __initialise_nx_graph(neighbour_matrix: dict):
        """
        Конструира nx граф от матрица на съседство.
        :param neighbour_matrix: dict, описващ съседните възли и теглата за всеки възел в графа.
        :return: g - конструиран nx граф, layout - dict с координати на възлите на графа.
        """
        g = nx.Graph()
        for node, neighbors in neighbour_matrix.items():
            for neighbor, weight in neighbors:
                g.add_edge(node, neighbor, weight=weight)
        pos = nx.spring_layout(g)
        return g, pos
