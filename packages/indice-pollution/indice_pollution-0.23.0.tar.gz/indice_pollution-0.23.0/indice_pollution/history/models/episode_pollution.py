from typing import List
from sqlalchemy.orm import relationship
from indice_pollution.history.models.commune import Commune
from indice_pollution.extensions import db
from datetime import datetime
from indice_pollution.helpers import today
from sqlalchemy import  Date, text

class EpisodePollution(db.Model):
    __table_args__ = {"schema": "indice_schema"}

    zone_id: int = db.Column(db.Integer, db.ForeignKey('indice_schema.zone.id'), primary_key=True, nullable=True)
    zone = relationship("indice_pollution.history.models.zone.Zone")
    date_ech: datetime = db.Column(db.DateTime, primary_key=True, nullable=True)
    date_dif: datetime = db.Column(db.DateTime, primary_key=True, nullable=True)
    code_pol: int = db.Column(db.Integer, primary_key=True)
    etat: str = db.Column(db.String)
    com_court: str = db.Column(db.String)
    com_long: str = db.Column(db.String)

    @classmethod
    def get(cls, insee=None, code_epci=None, date_=None):
        if insee:
            zone_subquery = Commune.get_query(insee=insee).limit(1).with_entities(Commune.zone_pollution_id).subquery()
        date_ = date_ or today()
        query = \
            cls.query.filter(
                cls.date_ech.cast(Date)==date_,
                cls.zone_id.in_(zone_subquery)
            )\
            .order_by(cls.date_dif.desc())
        return query.all()

    @classmethod
    def bulk_query(cls, insees=None, codes_epci=None, date_=None):
        return text(
            """
            SELECT
                DISTINCT ON (e.zone_id, e.date_ech) e.*, e.date_ech e, c.insee
            FROM
                indice_schema.episode_pollution e
                LEFT JOIN indice_schema.commune c ON c.zone_pollution_id = e.zone_id
                WHERE c.insee = ANY(:insees) AND date_ech=:date_ech
                ORDER BY e.zone_id, e.date_ech, e.date_dif DESC
            """
        ).bindparams(
            date_ech=date_,
            insees=insees
        )
    
    @classmethod
    def bulk(cls, insees=None, codes_epcis=None, date_=None):
        return db.session.execute(cls.bulk_query(insees=insees, date_=date_))

    @classmethod
    def get_all_query(cls, date_):
        return db.session.query(
                cls.zone_id, cls
            ).filter(
                cls.date_ech == date_
            ).order_by(
                cls.zone_id, cls.date_ech, cls.date_dif
            ).distinct(cls.zone_id, cls.date_ech)

    @classmethod
    def get_all(cls, date_):
        return dict(cls.get_all_query(date_).all())

    @property
    def lib_pol(self):
        return self.get_lib_pol(self.code_pol)

    @classmethod
    def get_lib_pol(cls, code_pol):
        return {
            1: 'Dioxyde de soufre',
            3: 'Dioxyde d’azote',
            4: 'Monoxyde de carbone',
            5: 'Particules PM 10',
            7: 'Ozone',
            8: 'Dioxyde d’azote',
            24: 'Particules PM10',
            39: 'Particules PM25',
        }.get(code_pol)

    @property
    def lib_pol_normalized(self):
        return self.get_lib_pol_normalized(self.code_pol)

    @classmethod
    def get_lib_pol_normalized(cls, code_pol):
        return {
            1: 'dioxyde_soufre',
            3: 'dioxyde_azote',
            5: 'particules_fines',
            7: 'ozone',
            8: 'dioxyde_azote',
            24: 'pm10',
            39: 'pm25',
        }.get(code_pol)

    @property
    def code_etat(self):
        return self.get_code_etat(self.etat)

    @classmethod
    def get_code_etat(cls, etat):
        etat = etat.lower()
        if "ssement" in etat:
            return 0
        elif "information" in etat:
            return 1
        elif "alerte" in etat:
            return 2
        else:
            return None

    @property
    def lib_etat(self):
        return self.get_lib_etat(self.code_etat)

    @classmethod
    def get_lib_etat(cls, code_etat):
        if  code_etat is None:
            return None
        return ["pas de dépassement", "information", "alerte"][code_etat]

    def dict(self):
        return {
            "code_pol": f"{self.code_pol:02}",
            "code_zone": self.zone.code if self.zone else "",
            "com_court": self.com_court,
            "com_long": self.com_long,
            "date": self.date_ech.date().isoformat(),
            "date_ech": self.date_ech.date().isoformat(),
            "date_dif": self.date_dif.date().isoformat(),
            "etat": self.etat,
            "lib_pol": self.lib_pol,
            "lib_pol_normalized": self.lib_pol_normalized
        }

    @classmethod
    def filter_etat_haut(cls, episodes):
        valid_etats = [e.code_etat for e in episodes if e.code_etat != None]
        if len(valid_etats) == 0:
            return []
        max_etat = max(valid_etats)
        if max_etat == 0:
            return []
        return [e for e in episodes if e.code_etat == max_etat]