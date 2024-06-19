declare module 'esptk' {
  class ESPFile {
    constructor(filePath: string);
    setLightFlag(enabled: boolean): void;
    isMaster: boolean;
    isMedium: boolean;
    isLight: boolean;
    isDummy: boolean;
    author: string;
    description: string;
    masterList: string[];
    revision: number;
  }
  export default ESPFile;
}
