from datetime import datetime
from typing import Annotated

from annotated_types import Gt
from pydantic import AnyHttpUrl, BaseModel, Field

from metmuseum.types.models.object_constituent import ObjectConstituent
from metmuseum.types.models.object_dimensions import ObjectDimensions
from metmuseum.types.models.object_measurementsElement import (
    ObjectMeasurementsElement,
)
from metmuseum.types.models.object_tag import ObjectTag


class ObjectResponse(BaseModel):
    id: Annotated[int, Gt(0)] = Field(alias="objectID")
    is_highlight: bool = Field(alias="isHighlight")
    accession_number: str = Field(alias="accessionNumber")
    accession_year: str = Field(alias="accessionYear")
    is_public_domain: bool = Field(alias="isPublicDomain")
    primary_image: AnyHttpUrl = Field(alias="primaryImage")
    primary_image_small: AnyHttpUrl = Field(alias="primaryImageSmall")
    additional_images: tuple[AnyHttpUrl, ...] = Field(alias="additionalImages")
    constituents: tuple[ObjectConstituent] = Field(alias="constituents")
    department: str = Field(alias="department")
    name: str = Field(alias="objectName")
    title: str = Field(alias="title")
    culture: str = Field(alias="culture")
    period: str = Field(alias="period")
    dynasty: str = Field(alias="dynasty")
    reign: str = Field(alias="reign")
    portfolio: str = Field(alias="portfolio")
    artist_role: str = Field(alias="artistRole")
    artist_prefix: str = Field(alias="artistPrefix")
    artist_display_name: str = Field(alias="artistDisplayName")
    artist_display_bio: str = Field(alias="artistDisplayBio")
    artist_suffix: str = Field(alias="artistSuffix")
    artist_alpha_sort: str = Field(alias="artistAlphaSort")
    artist_nationality: str = Field(alias="artistNationality")
    artist_begin_date: str = Field(alias="artistBeginDate")
    artist_end_date: str = Field(alias="artistEndDate")
    artist_gender: str = Field(alias="artistGender")
    artist_wikidata: AnyHttpUrl = Field(alias="artistWikidata_URL")
    artist_ulan: AnyHttpUrl = Field(alias="artistULAN_URL")
    date: str = Field(alias="objectDate")
    begin_date: int = Field(alias="objectBeginDate")
    end_date: int = Field(alias="objectEndDate")
    medium: str = Field(alias="medium")
    dimensions: str = Field(alias="dimensions")
    dimensions_parsed: tuple[ObjectDimensions, ...] = Field(
        alias="dimensionsParsed", default_factory=tuple
    )
    measurements: tuple[ObjectMeasurementsElement, ...] = Field(alias="measurements")
    credit_line: str = Field(alias="creditLine")
    geography_type: str = Field(alias="geographyType")
    city: str = Field(alias="city")
    state: str = Field(alias="state")
    county: str = Field(alias="county")
    country: str = Field(alias="country")
    region: str = Field(alias="region")
    subregion: str = Field(alias="subregion")
    locale: str = Field(alias="locale")
    locus: str = Field(alias="locus")
    excavation: str = Field(alias="excavation")
    river: str = Field(alias="river")
    classification: str = Field(alias="classification")
    rights_and_reproduction: str = Field(alias="rightsAndReproduction")
    link_resource: str = Field(alias="linkResource")
    metadata_date: datetime = Field(alias="metadataDate")
    repository: str = Field(alias="repository")
    url: AnyHttpUrl = Field(alias="objectURL")
    tags: tuple[ObjectTag, ...] = Field(alias="tags")
    wikidata: AnyHttpUrl = Field(alias="objectWikidata_URL")
    is_timeline_work: bool = Field(alias="isTimelineWork")
    Gallery_number: str = Field(alias="GalleryNumber")


__all__ = ("ObjectResponse",)
