def h_index():
    hindex = 0
    hindex_list = []
    hindex_list2 = []
    f = raw_input()
    list_of_citations = f.split(" ")
    for index in range(0, len(list_of_citations)):
        poped_item = list_of_citations.pop(0)
        print("Poped item {}".format(poped_item))
        list_of_citations.append(int(poped_item))
    list_of_citations.sort()
    print("input list {}".format(list_of_citations))
    max_citations = len(list_of_citations)
    counter = 1
    for x in list_of_citations:

        if x>=max_citations:
            hindex=max_citations
        else:
            max_citations-=1
        hindex_list.append(hindex)

    print("hindex List 1 {}".format(hindex_list))

    
    return hindex

print(h_index())