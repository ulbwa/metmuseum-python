from datetime import datetime
from typing import Annotated

from annotated_types import Gt, MinLen
from pydantic import BaseModel, Field, field_validator

from metmuseum.types import models


class ObjectResponse(BaseModel):
    id: Annotated[int, Gt(0)] = Field(alias="objectID")
    is_highlight: bool = Field(alias="isHighlight")
    accession_number: str = Field(alias="accessionNumber")
    accession_year: int | None = Field(alias="accessionYear")
    is_public_domain: bool = Field(alias="isPublicDomain")
    primary_image: Annotated[str, MinLen(1)] | None = Field(alias="primaryImage")
    primary_image_small: Annotated[str, MinLen(1)] | None = Field(
        alias="primaryImageSmall"
    )
    additional_images: tuple[str, ...] = Field(alias="additionalImages")
    constituents: tuple[models.ObjectConstituent, ...] | None = Field(
        alias="constituents"
    )
    department: str = Field(alias="department")
    name: str = Field(alias="objectName")
    title: str = Field(alias="title")
    culture: str = Field(alias="culture")
    period: str = Field(alias="period")
    dynasty: Annotated[str, MinLen(1)] | None = Field(alias="dynasty")
    reign: Annotated[str, MinLen(1)] | None = Field(alias="reign")
    portfolio: Annotated[str, MinLen(1)] | None = Field(alias="portfolio")
    artist_role: str = Field(alias="artistRole")
    artist_prefix: Annotated[str, MinLen(1)] | None = Field(alias="artistPrefix")
    artist_display_name: str = Field(alias="artistDisplayName")
    artist_display_bio: str = Field(alias="artistDisplayBio")
    artist_suffix: Annotated[str, MinLen(1)] | None = Field(alias="artistSuffix")
    artist_alpha_sort: str = Field(alias="artistAlphaSort")
    artist_nationality: str = Field(alias="artistNationality")
    artist_begin_date: int | None = Field(alias="artistBeginDate")
    artist_end_date: int | None = Field(alias="artistEndDate")
    artist_gender: str = Field(alias="artistGender")

    # I think we need to use validation with AnyHttpUrl,
    # but the API responses sometimes contain values like "(not assigned)",
    # so i can't be sure if there are other values that should also be handled as None.
    # This solution might cause issues later on
    artist_wikidata: Annotated[str, MinLen(1)] | None = Field(alias="artistWikidata_URL")
    artist_ulan: Annotated[str, MinLen(1)] | None = Field(alias="artistULAN_URL")

    date: str = Field(alias="objectDate")
    begin_date: int = Field(alias="objectBeginDate")
    end_date: int = Field(alias="objectEndDate")
    medium: str = Field(alias="medium")
    dimensions: str = Field(alias="dimensions")
    dimensions_parsed: tuple[models.ObjectDimensions, ...] = Field(
        alias="dimensionsParsed", default_factory=tuple
    )
    measurements: tuple[models.ObjectMeasurementsElement, ...] | None = Field(
        alias="measurements"
    )
    credit_line: str = Field(alias="creditLine")
    geography_type: Annotated[str, MinLen(1)] | None = Field(alias="geographyType")
    city: Annotated[str, MinLen(1)] | None = Field(alias="city")
    state: Annotated[str, MinLen(1)] | None = Field(alias="state")
    county: Annotated[str, MinLen(1)] | None = Field(alias="county")
    country: Annotated[str, MinLen(1)] | None = Field(alias="country")
    region: Annotated[str, MinLen(1)] | None = Field(alias="region")
    subregion: Annotated[str, MinLen(1)] | None = Field(alias="subregion")
    locale: Annotated[str, MinLen(1)] | None = Field(alias="locale")
    locus: Annotated[str, MinLen(1)] | None = Field(alias="locus")
    excavation: Annotated[str, MinLen(1)] | None = Field(alias="excavation")
    river: Annotated[str, MinLen(1)] | None = Field(alias="river")
    classification: str = Field(alias="classification")
    rights_and_reproduction: Annotated[str, MinLen(1)] | None = Field(
        alias="rightsAndReproduction"
    )
    link_resource: Annotated[str, MinLen(1)] | None = Field(alias="linkResource")
    metadata_date: datetime = Field(alias="metadataDate")
    repository: str = Field(alias="repository")

    # Should this value always contain a URL? If so, can we use AnyHttpUrl here?
    url: str = Field(alias="objectURL")

    tags: tuple[models.ObjectTag, ...] | None = Field(alias="tags")

    # I think we need to use validation with AnyHttpUrl,
    # but the API responses sometimes contain values like "(not assigned)",
    # so i can't be sure if there are other values that should also be handled as None.
    # This solution might cause issues later on
    wikidata: Annotated[str, MinLen(1)] | None = Field(alias="objectWikidata_URL")

    is_timeline_work: bool = Field(alias="isTimelineWork")
    gallery_number: Annotated[str, MinLen(1)] | None = Field(alias="GalleryNumber")

    @field_validator(
        "wikidata",
        "primary_image",
        "primary_image_small",
        "artist_wikidata",
        "artist_ulan",
        "artist_begin_date",
        "artist_end_date",
        "accession_year",
        "dynasty",
        "reign",
        "portfolio",
        "artist_prefix",
        "artist_suffix",
        "geography_type",
        "city",
        "state",
        "county",
        "country",
        "region",
        "subregion",
        "locale",
        "locus",
        "excavation",
        "river",
        "rights_and_reproduction",
        "link_resource",
        "gallery_number",
        mode="before",
    )
    def validate_empty_str_as_none(cls, v: str) -> str | None:
        if v == "":
            return None
        return v


__all__ = ("ObjectResponse",)
