using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.InputSystem;

public class RocketPosition : MonoBehaviour
{
    // Update is called once per frame
    void Update()
    {
        transform.position = new Vector3(GameManager.Instance.rocketX, GameManager.Instance.rocketY, 0);

    }

    void OnExit()
    {
        Debug.Log("exiting");
        Application.Quit();
        
    }
}
