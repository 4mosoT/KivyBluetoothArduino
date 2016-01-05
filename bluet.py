from kivy.utils import platform

if 'android' == platform:
    from jnius import autoclass, cast

    BluetoothAdapter = autoclass('android.bluetooth.BluetoothAdapter')
    BluetoothDevice = autoclass('android.bluetooth.BluetoothDevice')
    BluetoothSocket = autoclass('android.bluetooth.BluetoothSocket')
    PythonActivity = autoclass('org.renpy.android.PythonActivity')
    Intent = autoclass('android.content.Intent')

    UUID = autoclass('java.util.UUID')
    android = True

    bt_adapter = BluetoothAdapter.getDefaultAdapter()
    if not bt_adapter.isEnabled():
        intent = Intent(BluetoothAdapter.ACTION_REQUEST_ENABLE)
        currentActivity = cast('android.app.Activity', PythonActivity.mActivity)
        currentActivity.startActivityForResult(intent, 1)


else:
    android = False
    import bluetooth



def discover():
    if android:
        return [x.getName() for x in bt_adapter.getBondedDevices().toArray()]

    else:
        return bluetooth.discover_devices()

def get_name(mac):
    return bluetooth.lookup_name(mac)


def discover_thread(queue):
    discovered = discover()
    dict = {}
    for x in discovered:
        dict[x] = get_name(x)
    queue.put(dict)

