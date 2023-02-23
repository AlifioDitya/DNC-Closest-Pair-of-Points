from module.bruteforce import brute_force_closest_pair

def testBF(points):
    # Compare with brute force
    p1, p2 = brute_force_closest_pair(points)
    print("Minimum distance with BF :", p1.distance_to(p2))
    print("Closest pair of points with BF:", (p1,p2))
    print("")