import rospy
from braille_recognize.srv import braille_request, braille_requestResponse, braille_requestRequest

if (__name__ == '__main__'):
    rospy.init_node('dot_test_client')
    rospy.wait_for_service('braille_recognize')

    braille_client = rospy.ServiceProxy('braille_recognize', braille_request)
    request = braille_requestRequest()
    response = braille_client.call(request)

    print(response.array_length)
    print(response.number)
    print(response.position)