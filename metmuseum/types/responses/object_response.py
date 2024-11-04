from datetime import datetime
from typing import Annotated

from annotated_types import Gt
from pydantic import BaseModel, Field, field_validator

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
    accession_year: int | None = Field(alias="accessionYear")
    is_public_domain: bool = Field(alias="isPublicDomain")
    primary_image: str | None = Field(alias="primaryImage")
    primary_image_small: str | None = Field(alias="primaryImageSmall")
    additional_images: tuple[str, ...] = Field(alias="additionalImages")
    constituents: tuple[ObjectConstituent, ...] | None = Field(alias="constituents")
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
    artist_begin_date: int | None = Field(alias="artistBeginDate")
    artist_end_date: int | None = Field(alias="artistEndDate")
    artist_gender: str = Field(alias="artistGender")

    # I think we need to use validation with AnyHttpUrl,
    # but the API responses sometimes contain values like "(not assigned)",
    # so i can't be sure if there are other values that should also be handled as None.
    # This solution might cause issues later on
    artist_wikidata: str | None = Field(alias="artistWikidata_URL")
    artist_ulan: str | None = Field(alias="artistULAN_URL")

    date: str = Field(alias="objectDate")
    begin_date: int = Field(alias="objectBeginDate")
    end_date: int = Field(alias="objectEndDate")
    medium: str = Field(alias="medium")
    dimensions: str = Field(alias="dimensions")
    dimensions_parsed: tuple[ObjectDimensions, ...] = Field(
        alias="dimensionsParsed", default_factory=tuple
    )
    measurements: tuple[ObjectMeasurementsElement, ...] | None = Field(
        alias="measurements"
    )
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

    # Should this value always contain a URL? If so, can we use AnyHttpUrl here?
    url: str = Field(alias="objectURL")

    tags: tuple[ObjectTag, ...] | None = Field(alias="tags")

    # I think we need to use validation with AnyHttpUrl,
    # but the API responses sometimes contain values like "(not assigned)",
    # so i can't be sure if there are other values that should also be handled as None.
    # This solution might cause issues later on
    wikidata: str | None = Field(alias="objectWikidata_URL")

    is_timeline_work: bool = Field(alias="isTimelineWork")
    Gallery_number: str = Field(alias="GalleryNumber")

    @field_validator(
        "wikidata",
        "primary_image",
        "primary_image_small",
        "artist_wikidata",
        "artist_ulan",
        "artist_begin_date",
        "artist_end_date",
        "accession_year",
        mode="before",
    )
    def validate_empty_str_as_none(cls, v: str) -> str | None:
        if v == "":
            return None
        return v


__all__ = ("ObjectResponse",)
