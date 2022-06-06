Engine.DI.DIContainer.RegisterAsSingle
============================

Here we register just one value, Always override the value to the last VALUE added.


.. code-block:: csharp

    public void Inject()
    {
        Engine.DI.DIContainer.RegisterAsSingle<ICoinsData>(this);
    }
    
Лучшая практика инжектить через ``MomoInjector``.
По умолчанию лежит на сцене ``Main`` в объекте Managers.

.. image:: img/MomoInjector.png
       :scale: 100 %
       :align: center
