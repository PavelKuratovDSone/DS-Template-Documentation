Physic.RaycastHits.GetColliderHitedRaycast
============================

.. code-block:: csharp

    public class GetColliderHitedRaycastExample : MonoBehaviour
    {
            private void Update()
            {
                if (ControllerInputs.OnMouse(MouseStatue.Down))
                {
                    
                        Debug.Log(Physic.RaycastHits.GetColliderHitedRaycast<BoxCollider>(Camera.main, UnityEngine.Input.mousePosition));
                }
            }
    }
