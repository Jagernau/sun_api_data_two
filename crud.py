from sqlalchemy.orm import Session, outerjoin
from mysql_models import *
from sqlalchemy import case


def get_all_objects(db: Session):
    result = db.query(
                CaObject.id,
                MonitoringSystem.mon_sys_name,
                CaObject.object_name,
                ObjectStatus.status,
                CaObject.owner_user,
                CaObject.imei,
                Device.device_serial,
                DevicesBrand.name.label('brand_name'),
                SimCard.sim_tel_number,
                case(
                    [
                        (SimCard.status == 0, "Списана"),
                        (SimCard.status == 1, "Активна"),
                        (SimCard.status == 2, "Приостановлена"),
                        (SimCard.status == 3, "Первичная блокировка"),
                        (SimCard.status == 4, "Статус не известен"),
                    ]
                ).label("sim_status"),
                CellOperator.name.label("cell_operator"),
                Contragent.ca_uid_contragent,
                Contragent.ca_name_contragent,
                Contragent.ca_inn,
                Contragent.ca_kpp,
                Contragent.key_manager,
                Contragent.service_manager,
                CaObject.ok_desk_id.label("obj_ok_id"),
                Contragent.ok_desk_id.label("contragent_ok_id"),

            ).outerjoin(
                MonitoringSystem, CaObject.sys_mon_id == MonitoringSystem.mon_sys_id
            ).outerjoin(
                ObjectStatus, CaObject.object_status == ObjectStatus.status_id
            ).outerjoin(
                Device, CaObject.imei == Device.device_imei
            ).outerjoin(
                DevicesBrand, Device.devices_brand_id == DevicesBrand.id
            ).outerjoin(
                SimCard, CaObject.imei == SimCard.terminal_imei
            ).outerjoin(
                CellOperator, SimCard.sim_cell_operator == CellOperator.id
            ).outerjoin(
                Contragent, CaObject.contragent_id == Contragent.ca_id
            ).order_by(CaObject.id.desc()).limit(20).all()
    db.close()
    return result

