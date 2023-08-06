"""
-----------------------------------------
@Author: xuhuanjun
@Email: 20212010075@fudan.edu.cn
@Created: 2021/11/1
------------------------------------------
@Modify: 2021/11/1
------------------------------------------
@Description:
"""
from kgdt.models.graph import GraphData


class SoftwareKG:
    def __init__(self, graph_path):
        self.graph: GraphData = GraphData.load(graph_path)

    def is_exist_concept(self, word):
        if self.graph.find_nodes_by_property("concept_name", word) is None:
            return False
        return True

    def get_node_num(self):
        return self.graph.get_node_num()

    def get_node_ids(self):
        return self.graph.get_node_ids()

    def print_graph_info(self):
        return self.graph.print_graph_info()

    def get_node_info_by_id(self, nodeid):
        return self.graph.get_node_info_dict(nodeid)

    def get_node_by_concept(self, word):
        return self.graph.find_nodes_by_property("concept_name", word)

    def get_id_by_concept(self, word):
        node = self.graph.find_nodes_by_property("concept_name", word)
        return node[0]['id']

    def get_concept_score(self, word):
        node = self.graph.find_nodes_by_property("concept_name", word)
        return node[0]['properties']['score']

    def get_concept_labels(self, word):
        node = self.graph.find_nodes_by_property("concept_name", word)
        return node[0]['labels']

    def is_exist_is_a_relation(self, start_word, end_word, relationtype='is a'):
        start_id = self.get_id_by_concept(start_word)
        end_id = self.get_id_by_concept(end_word)
        return self.graph.exist_relation(startId=start_id, relationType=relationtype, endId=end_id)

    def get_in_relations(self, concept):
        id = self.get_id_by_concept(concept)
        return self.graph.get_all_in_relations(id)

    def get_out_relations(self, concept):
        id = self.get_id_by_concept(concept)
        return self.graph.get_all_out_relations(id)

    def is_exit_facet_of_relation(self, start_word, end_word, relationtype='facet of'):
        start_id = self.get_id_by_concept(start_word)
        end_id = self.get_id_by_concept(end_word)
        return self.graph.exist_relation(startId=start_id, relationType=relationtype, endId=end_id)

    def is_exit_relation(self, start_word, end_word):
        start_id = self.get_id_by_concept(start_word)
        end_id = self.get_id_by_concept(end_word)
        return self.graph.exist_any_relation(start_id, end_id)

    def get_all_relations(self, start_word, end_word):
        start_id = self.get_id_by_concept(start_word)
        end_id = self.get_id_by_concept(end_word)
        return self.graph.get_all_relations(start_id, end_id)

    def find_all_shortest_paths(self, start_word, end_word):
        start_id = self.get_id_by_concept(start_word)
        end_id = self.get_id_by_concept(end_word)
        return self.graph.find_all_shortest_paths(start_id, end_id)

    def find_common_out_relationship_node(self, concept1, concept2):
        concept1_id = self.get_id_by_concept(concept1)
        concept2_id = self.get_id_by_concept(concept2)

        concept1_relations = self.graph.get_all_out_relations(concept1_id)
        concept2_relations = self.graph.get_all_out_relations(concept2_id)

        comment_relations = []
        for relation1 in concept1_relations:
            for relation2 in concept2_relations:
                if relation1[2] == relation2[2] and relation1[1] == relation2[1]:
                    comment_relations.append(relation2[1])
        return comment_relations

    def find_common_in_relationship_node(self, concept1, concept2):
        concept1_id = self.get_id_by_concept(concept1)
        concept2_id = self.get_id_by_concept(concept2)

        concept1_relations = self.graph.get_all_in_relations(concept1_id)
        concept2_relations = self.graph.get_all_in_relations(concept2_id)

        comment_relations = []
        for relation1 in concept1_relations:
            for relation2 in concept2_relations:
                if relation1[0] == relation2[0] and relation1[1] == relation2[1]:
                    comment_relations.append(relation2[0])
        return comment_relations
